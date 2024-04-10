
export const Nav=(props)=>{
    const list=[]
    for(let i =0;i<props.data.length;i++){
        let t= props.data[i];
        list.push(<li key={t.id}>
            <a id={t.id} href={'/read/'+t.id} onClick={event=>{
                event.preventDefault(); 
                props.onchangeMode(Number(event.target.id));
                }}>{t.title}
            </a>
            </li>)
    };
    
    return(
        <nav>
            <ol>
                {list}
            </ol>
        </nav>
    );
}


