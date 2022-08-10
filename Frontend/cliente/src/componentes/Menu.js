import React, { useState } from 'react'
import { NavLink } from 'react-router-dom'
import { Asistencia_docente } from './Asistencia_docente'
import { Asistencia_pasante } from './Asistencia_pasante'
import { Asistencia_miembro_eq  } from './Asistencia_miembro_eq'
import { Generar_reportes } from './Generar_reportes'


export const Menu = (props) => {

  const [asisdoc, setAsisdoc] = useState("");
  const [asispas, setAsispas] = useState("");
  const [asismmb, setAsismmb] = useState("");
  const [genrep, setGenrep] = useState("");

  function op_asisdoc(){
    setAsisdoc("1");
    setAsispas("0");
    setAsismmb("0");
    setGenrep("0");
  }
  function op_asispas(){
    setAsisdoc("0");
    setAsispas("1");
    setAsismmb("0");
    setGenrep("0");
  }
  function op_asismmb(){
    setAsisdoc("0");
    setAsispas("0");
    setAsismmb("1");
    setGenrep("0");
  }
  function op_genrep(){
    setAsisdoc("0");
    setAsispas("0");
    setAsismmb("0");
    setGenrep("1");
  }
  return (
    <>    
    <div id="caja_menu" style={{textAlign:"left"}}>
      <strong className="h3">
         Bienvenido Usuario : {props.cod_log.toUpperCase()} 
      </strong>
      <nav className="navbar navbar-expand-lg navbar-light bg-light" style={{marginTop:20}}>
          <div className="container-fluid">

            <label className="navbar-brand  h5" href=" ">Menú Principal</label>
            
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div className="navbar-nav">
                <NavLink to="" className="nav-link  h5  text-center" onClick={ op_asisdoc } >Asistencia Docente</NavLink>
                <NavLink to="" className="nav-link  h5  text-center" onClick={ op_asispas } >Asistencia Pasante</NavLink>
                <NavLink to="" className="nav-link  h5  text-center" onClick={ op_asismmb } >Asistencia Miembro Equipo</NavLink>
                <NavLink to="" className="nav-link  h5  text-center" onClick={ op_genrep } >Generar reportes</NavLink>
                <a className="nav-link  h5  text-center"  style={{color:"blue"}}  href=" "  >Cerrar Sesión</a>
              </div>
            </div>
          </div>
        </nav>        
    </div>

    { asisdoc === "1" && <Asistencia_docente/>}
    { asispas === "1" && <Asistencia_pasante/>}
    { asismmb === "1" && <Asistencia_miembro_eq/>}
    { genrep === "1" && <Generar_reportes/>}

    </>
  )
}
