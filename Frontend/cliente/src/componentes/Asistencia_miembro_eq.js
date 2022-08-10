import React from 'react'

export const Asistencia_miembro_eq = () => {
  return (

<div className="h3">
  Asistencia Miembro Equipo
  <br/>
  <form id="miFormulario"  >
    <div className="row" style={{marginTop:20}}>
      <div className="col-6">
        <input className="form-control form-control-lg text-center" type="text" placeholder="Digite El Codigo Del Estudiante" required  />
      </div>
    
      <div className="col-6">
        <input className="form-control form-control-lg text-center" type="text" placeholder="Digite El Codigo Del Equipo" required  />
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
