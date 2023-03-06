import { useRef, useEffect } from "react";
import jSuites from "jsuites";
 
import "jsuites/dist/jsuites.css";
 
export default function Editor({ options }) {
  const editorRef = useRef(null);
 
  useEffect(() => {
    jSuites.editor(editorRef.current, options);
  }, [options]);
 
  return <div ref={editorRef} />;
}