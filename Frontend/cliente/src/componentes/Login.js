import React, { useState } from 'react'
import { Menu } from './Menu'

export const Login = () => {

  const [logeoActual, setLogeoactual] = useState("False")
  const [cod_log, setUsu] = useState("");

  const [data, setData] = useState({ data: [] });
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState('');

  const handleClick = async (e) => {
    e.preventDefault();
    try {
      var txtcod = document.getElementById("txtcod").value;
      await fetch('http://127.0.0.1:5000/login/' + txtcod,{
        method: 'GET',
        headers: {
          Accept: '*/*',
          'Accept-Encoding':'gzip, deflate, br',
          'Access-Control-Allow-Origin': '*',
        },
      })
      .then(response => response.json())
      .then(data => {
        if(data.login){
          setUsu(data);
          setLogeoactual("true");
          document.getElementById("form_login").style.display = "none";
        }else{
          setLogeoactual("false");
          alert("ERROR DE USUARIO");
          document.getElementById("txtcod").value = "";
          document.getElementById("txtcod").focus();
        }
        
      });

    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (

    <div className="container" style={{ background: "lightgray", marginTop: 20, padding: 20 }}>
      <form id="form_login">
        <div>
          <h1 style={{ color: "blue", textalign: "center" }}>LOGIN</h1>
        </div>
        <div>
          <label htmlFor="txtcod"><strong>Codigo empleado</strong></label>
          <input type="codigo" id="txtcod" style={{ textAlign: "center" }} className="form-control" required />
        </div><br />
        <input type="submit" className="btn btn-primary" value="Login" onClick={handleClick} />
      </form>

      {logeoActual === "true" && <Menu cod_log={cod_log} />}
    </div>
  )
}
