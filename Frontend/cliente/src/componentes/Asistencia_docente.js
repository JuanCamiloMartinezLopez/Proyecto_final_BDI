import React from 'react'

export const Asistencia_docente = () => {
  return (

<div className="h3">
  Asistencia Docente
  <br/>
  <form id="miFormulario"  >
    <div className="row" style={{marginTop:20}}>
      <div className="col-6">
        <input className="form-control form-control-lg text-center" type="text" placeholder="Digite Los Nombres Del Docente" required  />
      </div>
    
      <div className="col-6">
        <input className="form-control form-control-lg text-center" type="text" placeholder="Digite Los Apellidos Del Docente" required  />
      </div>
    </div>

    <div className="row" style={{marginTop:20}}>
      <div className="col">
        <button className="btn btn-primary btn-lg">Consulta</button>
      </div>
    </div>
  </form>
</div>
 
  )
}
