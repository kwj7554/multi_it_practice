const user={};
// 이름 : 5글자까지만 입력
let nameInput = document.signupForm.name;
nameInput.addEventListener('blur',()=>{
    nameInput.value=nameInput.value.replace(" ","");
    if(nameInput.value.length>5){
        alert('5글자 이내만 가능합니다');
        nameInput.value="";
        nameInput.focus();
    }
    user.name=nameInput.value
})

// 아이디 : 5~16글자까지 제한,소문자로 저장, 중복여부 체크
let idInput = document.signupForm.id;
idInput.addEventListener('blur',()=>{
    idInput.value=idInput.value.replace(" ","").toLowercase();
    if(idInput.value.length<5 || idInput.value.lenth>16){
        alert('5자리에서 16자리까지만 가능합니다.');
        idInput.value="";
    }
    user.id=idInput.value;
})
// 비밀번호 : 10~16자리 문자, 숫자, ~!@#$%^&*
let pwdInput = document.signupForm.pwd;
pwdInput.addEventListener('blur',()=>{
    pwdInput.value=pwdInput.value.trim();
    if(pwdInput.value.length<10 || pwdInput.value.length>16){
        alert('10자리에서 16자리까지만 가능합니다.');
        pwdInput.value="";
    }
    user.pwd=pwdInput.value;
})

// 비밀번호 확인 : 일치 여부 체크
let pwdCheckInput = document.signupForm.pwdChk;
pwdCheckInput.addEventListener('blur',()=>{
    pwdCheckInput.value=pwdCheckInput.value.trim();
    if(pwdCheck.vlaue != pwdInput ){
        alert('비밀번호가 다릅니다.');
        pwdInput.value="";
    }
    user.pwdChk=pwdCheckInput.value;
})

// 이메일 직접입력 : 주소 빈 칸 설정 및 작성 가능 처리


// 이메일 선택 : 주소 자동기입 및 읽기전용 처리


// 회원가입 버튼 클릭 시 : 이동하지 않고 객체로 값 가져오기