import './App.css';
import React, { useState } from 'react'
import { Header} from './components/Header';
import { Nav } from './components/Nav';
import { Article } from './components/Article';
import { Create } from './components/Create';

function App() {
  const [mode, setMode]=useState(null);
  const [id, setId]=useState(null)
  let content=null;
  const [data, setData] = useState([
    {id:1,title:"html",content:"html은 너무 편해요"},
    {id:2,title:"JS",content: "JS는 너무 어려워요"},
    {id:3,title:"Node.js", content:"Node.js는 너무 복잡해요"},
    {id:4,title:"CSS",content:"CSS는 헷갈려요"},
  ]);
  const [nextId, setNextId] = useState(5);
  if(mode === "Welcome"){
    content = <>
                <Article title="Welcome" body="Hello, React"></Article>
                <button onClick={()=>
                  setMode("Create")
                }>Create</button>
                </>
  }else if(mode ==="Read"){
    let title, body = null;
    for(let i =0;i<data.length;i++){
      if(data[i].id===id){
        title = data[i].title;
        body = data[i].content;
      }
    }
    content =<>
      <Article title={title} body={body}></Article>
      <button>update</button><button>delete</button>
    </>
  }else if(mode ==="Create"){
    content=<Create onCreate={(title, content)=>{
      const newData = {id:nextId,title:title,content:content}
      const copy=[...data]
      copy.push(newData)
      setData(copy)
      setMode("Read")
      setId(nextId)
      setNextId(nextId+1)
    }}></Create>
  }
  return (
    <>
      <Header title="react" onChangeMode={()=>{setMode("Welcome")}}></Header>
      <Nav data={data} onchangeMode={(id)=>{setMode("Read"); setId(id)}}></Nav>
      {content}
    </>
    
  );
}

export default App;
