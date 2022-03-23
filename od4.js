
const http = require('http');

const server = http.createServer((req, res) => {
    const url = req.url;

    if (url === '/') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<h2>Hakan T</h2>');
    }
    else if (url  === 'about') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<h2>Hakkimda </h2>')
    }
    else if (url  === 'contact') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<h2>Iletisim </h2>')
    }
    else{
        res.writeHead(404,{"Content-Type":"text/html"});
        res.write('<h2>bulamadık dayı...</h2>')

    }

    res.end();
})

const port = 3000;
server.listen(port,()=>{
    console.log(`Sunucu ${port} da çalışmaya başladı`)
})
