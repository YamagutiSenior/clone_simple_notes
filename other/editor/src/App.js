import logo from './logo.svg';
import './App.css';
import { Container } from "semantic-ui-react";
import Foo from "./Foo"

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          This App Contains Vulnerability 
          <br></br>
        <a
          className="App-link"
          href="https://www.cve.org/CVERecord?id=CVE-2022-25979"
          target="_blank"
          rel="noopener noreferrer"
        >
          CVE-2022-25979
        </a>
        </p>
        <p>
        scroll down......
        </p>
      </header>

      <Container>
        <Foo/>
      </Container>

    </div>
  );
}

export default App;
