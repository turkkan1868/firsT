const fs = require('fs')
const writeFile = (file, data) => {
return new Promise((resolve, reject) => {
fs.writeFile(file, data, 'utf8', (err) => {
if (err) reject(err)
resolve("Yazma başarılı : " + data)
})
})
}
const readFile = (file) => {
return new Promise((resolve, reject) => {
fs.readFile(file, 'utf8', (err,data) => {
if (err) reject(err)
resolve(data)
})
})
}
const appendFile = (file, data) => {
return new Promise((resolve, reject) => {
fs.appendFile(file, '\n' + data, 'utf8', (err) => {
if (err) reject(err)
resolve("Güncelleme başarılı : " + data)
})
})
}
const deleteFile = (file) => {
return new Promise((resolve, reject) => {
fs.unlink(file, (err) => {
if (err) reject(err)
resolve("Silme başarılı")
})
})
}
const islem = async () => {
await writeFile("employees.json", '{ "name": "Test", "salary": 2000 }').
then((result)=>{console.log(result)}).
catch((err)=>{console.log(err)});
await readFile("employees.json").
then((result)=>{console.log(result)}).
catch((err)=>{console.log(err)});
await appendFile("employees.json", '{ "name": "Halil Bey", "salary": 100100 }').
then((result)=>{console.log(result)}).
catch((err)=>{console.log(err)});
await deleteFile("employees.json").
then((result)=>{console.log(result)}).
catch((err)=>{console.log(err)});
}
islem();
