export const Create = (props) => {
    return ( 
    <>
        <h2>Create</h2>
        <form onSubmit={(event)=>{
            event.preventDefault();
            const title = event.target.title.value;
            const content = event.target.content.value;
            props.onCreate(title,content)
        }}>
            <p><input type="text" name="title" placeholder='title' /></p>
            <p><textarea name="content" placeholder='content'></textarea></p> 
            <p><input type='submit' value="Create"/></p>
        </form>  
    </> );
}
