const fs= require('fs').promises;
// 콜백 지옥에 빠지지 않기 위하여 promises로 반환하게 만들었다.
const constants = require('fs').constants;
// fs모듈에서 가지고 있는 상수들을 담고있는 객체

fs.access("./example",constants.F_OK | constants.W_OK | constants.R_OK)
//access는 파일이 있다면 접근하는 것이기 때문에 존재한다면 then으로 갈 것이다.    
    .then(()=>{
        return Promise.reject("이미 파일이 존재합니다.")
    })
    .catch((err)=>{
        if(err.code==="ENOENT"){
            // 존재하지 않아 발생하는 에러 코드가 ENOENT이다.
            console.log("폴더가 존재하지 않습니다.");
            return fs.mkdir("./example")
            // mkdir메소드로 파일을 만든다.
        }
        return Promise.reject(err)
    })
    .then(()=>{
        console.log("폴더를 만들었습니다.");
        return fs.open('./example/example.txt','w');
        // 폴더를 만들었으니 txt 파일을 만들고 쓰기 모드로 가져옵니다.
        // open-> 존재 하지 않다면 만들어서 가져옵니다. "r"로 읽기로 가져올 수 도있습니다.
    })
    .then((file)=>{
        console.log("빈 파일을 만들었습니다.");
        return fs.rename('./example/example.txt','./example/practice.txt');
        // example.txt파일 이름을 practice로 바꾸었습니다.
    })
    .catch((err)=>{
        console.error(err);
    })
setTimeout(()=>{
    fs.readdir('./example')
// example 폴더안에 존재하는 파일을 배열에 넣어 보여준다.
    .then((dir)=>{
        console.log("존재하는 파일 : ", dir); //["practice.txt"]
        return fs.unlink('./example/practice.txt');
        // txt 파일을 지운다
    })
    .then(()=>{
        console.log("파일을 삭제했다");
        return fs.rmdir('./example');
        // 폴더를 지운다.
    })
    .then(()=>{
        console.log("폴더를 삭제했다.");
    })
    .catch((err)=>{
        console.error(err)
    })
},1000)

