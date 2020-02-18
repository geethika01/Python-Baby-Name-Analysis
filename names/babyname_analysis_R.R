rm(list= ls())

library(dplyr)
library(stringr)

setwd("C:/Users/geethika.wijewardena/Workspace/Python/Python-Baby-Name-Analysis/names")

file_lst <- list.files(pattern = ".*.txt")

dat <- read.csv(file_lst[1], stringsAsFactors = F, na.strings = c(""), 
                col.names = c('babyname', 'sex', 'count'),
                colClasses = c('character','character', 'integer'))
dat['year'] <- as.factor(str_sub(file_lst[1], 4,7))

for (file in file_lst){
  df <- read.csv(file_lst[1], stringsAsFactors = F, na.strings = c(""), 
                 col.names = c('babyname', 'sex', 'count'),
                 colClasses = c('character','character', 'integer'))
  df['year'] <- as.integer(str_sub(file_lst[1], 4,7))
  dat <- rbind(dat,df)
}

skimr::skim(dat)
write.csv(dat, 'babynames.csv', row.names= F)
