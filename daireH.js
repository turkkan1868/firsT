
let arguments = process.argv.slice(2);

const daireAlanV = (r) => {
    const formul = Math.PI
    const result = formul * r**2;
    console.log(result)
}

daireAlanV(arguments[0]*1);