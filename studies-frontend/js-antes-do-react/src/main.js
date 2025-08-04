// Nullish Coalescing Operator

// const idade = 0;
// document.body.innerText = 'Sua idade é: ' + (idade ?? 'Não informado');

//Objectos

const user = {
    name: 'Kauan',
    idade: 17,
    address: {
        street: 'R.JBC',
        number: 87,
    },
};

document.body.innerText = ('name' in user)