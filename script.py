import os
import sys
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import natsort
import re

outpath = "TASK_2" + os.sep + "JSON" + os.sep + "Individual JSONs"


dflist = []
for jsonindex in natsort.natsorted(os.listdir(outpath)):
    if "feat" not in jsonindex and "ft" not in jsonindex:
        with open(outpath + os.sep + jsonindex) as f:
            data = json.load(f)
        if data:
            dfname = re.sub("_.*", "", jsonindex)
            df = pd.json_normalize(data)
            globals()[dfname] = df
            dflist.append(dfname)


dfplotrows = []
for dataset in dflist:
    row = []
    row.append(eval(dataset)["artist.name"][0] + " " + dataset)
    row.append(eval(dataset)["chordsPresent"].sum())
    row.append(eval(dataset)["chordsPresent"].count() -
               eval(dataset)["chordsPresent"].sum())
    row.append(eval(dataset)["chordsPresent"].count())
    dfplotrows.append(row)

dfplot = pd.DataFrame(dfplotrows, columns=[
                      "Artist Name", "Chords Present", "Chords Missing", "Total Entries"])
dfplot.set_index(dfplot["Artist Name"], drop=True, inplace=True)
dfplot.drop("Artist Name", axis=1, inplace=True)


dfplot.plot.barh(
    y=["Chords Present", "Chords Missing"],
    stacked=True,
    color={"Chords Present": "orange", "Chords Missing": "black"}
)
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.show()
