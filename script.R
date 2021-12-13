require(tidyverse)
require(ggplot2)
require(rayshader)
require(plot3D)
require(plot3Drgl)
require(RColorBrewer)


tilde <- rawToChar(as.raw(126)) # workaround for tilde bug

df <- read.csv(file = "Data-Science\\Python_1st_part\\anime project.csv", header = TRUE)
df$scoresquared <- df[, "score"]^2

summary(df)


ggplot(df[, c(1, 3:7, 9)], aes(x = reorder(anime_name, -score), score)) +
    geom_bar(stat = "identity")


anime_gg <- ggplot(df) +
    geom_point(aes(x = rank, color = scoresquared, y = popularity), size = 2) +
    scale_color_continuous(limits = c(0, 100)) +
    ggtitle("Anime Rank Vs. Popularity, colorscale by (Score)^2") +
    theme(title = element_text(size = 8), text = element_text(size = 12))
anime_gg

anime_rain <- anime_gg +
    scale_color_gradientn(colours = rainbow(100))

anime_rain

plot_gg(anime_rain, height = 10, width = 10, multicore = TRUE, pointcontract = 0.7, soliddepth = -200)