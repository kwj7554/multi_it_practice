const add_btn =document.querySelector("#addbutton");
const com_input = document.querySelector("#comment");
const com_list = document.querySelector("#comment_list");

//초기 대이터 가져오기

fetch("./data/comment.json")
    .then(response=>{
        if(response.ok) return response.json();
    })
    .then(comments =>{
        console.log(comments);
    })



// function createCmtElement(comment){
//     const li = document.createElement("li");
//     li.classList.add(comment);
//     li.innerHTml=`
//                 <div class="comment-box">
//                     <div>${comment.name} : ${comment.msg}-${comment.date}</div>
//                     <div class="actions">
//                         <button class="edit">수정</button>
//                         <button class="delete">삭제</button>
//                     </div>
//                 </div>

//                 <div class="edit-box">
//                     <input type="text" value='${comment.msg}' />
//                     <button class="save">저장</button>
//                 </div>
//                     `;
//     const editBtn = document.querySelector('.edit');
//     const delBtn = document.querySelector('.delete');
//     const saveBtn = documnent.querySelector('.save');
//     const editBox = document.querySelector('.edit-box');
//     const comBox = document.querySelector('.comment-box');
//     const newcomInput = document.querySelector("input")

//     editBox.style.display ="none";

//     editBtn.addEventListener("click",()=>{
//         comBox.style.display ="none";
//         editBox.style.display = "inline";    
//     })

//     // saveBtn.addEventListener("click",()=>{
//     //     comment.msg=newcomInput.value;
//     //     fetch("./data/comment.json/comments"+)
//     // })

// }