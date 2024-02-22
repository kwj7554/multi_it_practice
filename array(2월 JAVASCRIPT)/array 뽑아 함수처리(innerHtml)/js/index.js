const rowString = document.querySelector('h1').innerText;
const originArr=rowString.slice(rowString.indexOf('[')+1,rowString.indexOf(']')).split(', ');
console.log(originArr);

const originDiv = document.querySelector('#origin');
const resultDiv = document.querySelector('#result');


originDiv.innerHTML=showArray(originArr);

let sum=0;
for(let i of originArr){
    sum=sum+Number(i);
}
originArr.push(sum);
resultDiv.innerHTML=showArray(originArr);


function showArray(array){
    let htmlCode ='<table><tr>';
    for(let i of array){
        htmlCode+=`<td>${i}</td>`;
    }
    htmlCode=htmlCode +"</tr></table>"
    return htmlCode;
}