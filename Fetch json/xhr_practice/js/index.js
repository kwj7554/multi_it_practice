function loadStudents(){
    return fetch("./data/students.json")
        .then((response)=>response.json())
        .then((json)=> json.students);
}

loadStudents().then((students)=>{
    console.log(students);
    const resultDiv =document.querySelector("#result");
    const resultSet = randomSelect(students, 3);
    for (const student of resultSet) {
        const studentDiv = document.createElement('div');
        studentDiv.classList.add('student');
        studentDiv.innerHTML = createHTMLstring(student);
        resultDiv.appendChild(studentDiv);
    }
})

function randomSelect(arr, count) {
    const resultSet = new Set([]);

    while (resultSet.size != count) {
        const randomIdx = Math.floor(Math.random() * arr.length);
        resultSet.add(arr.splice(randomIdx, 1)[0])
    }
    return resultSet;
}

function createHTMLstring(arr){
    return `
    <p>${arr.name}</p>
    <p>성별 : ${arr.gender}</p>
    <p>주소 : ${arr.address}</p>
`;
}