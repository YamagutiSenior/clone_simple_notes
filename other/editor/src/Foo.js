import Editor from "./Editor";

import 'reactjs-popup/dist/index.css';

export default function Foo() {
  return (
    <>
      <h3>Editor:</h3>
      <Editor
        options={{
          value: "",
          allowToolbar: true,
          border: true,
          padding: true,
          parseURL: true,
          toolbar: [{
            content: 'yo',
            onclick: function() {
              window.alert("Yoooo!");
          }  
        }]
        }}
      />
    </>
  );
}