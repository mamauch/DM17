library(cluster)
getwd()

datadim032 = read.table("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/data/dim032.txt")
datas2 = read.table("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/data/s2.txt")
dataseeds = read.table("/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/data/seeds_dataset.txt")


ang1dim032 <- agnes(datadim032, metric = "euclidean", method = "complete")
ang2dim032 <- agnes(datadim032, metric = "manhattan", method = "complete")
ang3dim032 <- agnes(datadim032, metric = "euclidean", method = "average")
dv1dim032 <- diana(datadim032, metric = "manhattan")
dv2dim032 <- diana(datadim032, metric = "euclidean")

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang1dim032.png")
plot(ang1dim032)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang2dim032.png")
plot(ang2dim032)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang3dim032.png")
plot(ang3dim032)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv1dim032.png")
plot(dv1dim032)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv2dim032.png")
plot(dv2dim032)
dev.off()

ang1datas2 <- agnes(datas2, metric = "euclidean", method = "complete")
ang2datas2 <- agnes(datas2, metric = "manhattan", method = "complete")
ang3datas2 <- agnes(datas2, metric = "euclidean", method = "average")
dv1datas2 <- diana(datas2, metric = "manhattan")
dv2datas2 <- diana(datas2, metric = "euclidean")

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang1datas2.png")
plot(ang1datas2)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang2datas2.png")
plot(ang2datas2)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang3datas2.png")
plot(ang3datas2)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv1datas2.png")
plot(dv1datas2)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv2datas2.png")
plot(dv2datas2)
dev.off()


ang1dataseeds <- agnes(dataseeds, metric = "euclidean", method = "complete")
ang2dataseeds <- agnes(dataseeds, metric = "manhattan", method = "complete")
ang3dataseeds <- agnes(dataseeds, metric = "euclidean", method = "average")
dv1dataseeds <- diana(dataseeds, metric = "manhattan")
dv2dataseeds <- diana(dataseeds, metric = "euclidean")

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang1dataseeds.png")
plot(ang1dataseeds)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang2dataseeds.png")
plot(ang2dataseeds)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/ang3dataseeds.png")
plot(ang3dataseeds)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv1dataseeds.png")
plot(dv1dataseeds)
dev.off()

png(filename="/Users/Marius/Documents/Studium/Mainz/DM17/Uebung4/output/dv2dataseeds.png")
plot(dv2dataseeds)
dev.off()



