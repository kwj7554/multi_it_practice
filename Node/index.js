const fs =require('fs').promises

fs.rmdir('./example')
    .then(()=>{
        console.log("파일을 삭제했다");
    })
    .catch(()=>{
        console.log("파일을 못 삭제했다");
    })