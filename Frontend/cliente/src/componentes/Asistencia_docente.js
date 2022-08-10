import React,{ useState } from 'react'

export const Asistencia_docente = () => {

  const [curso, setCurso] = useState([]);

  const handleClick = async (e) => {
    e.preventDefault();
    try {
      var nom = document.getElementById("nombre").value;
      var apell = document.getElementById("apellido").value;
      await fetch('http://127.0.0.1:5000/asistencia_docente/' + nom + '/' + apell, {
        method: 'GET',
        headers: {
          Accept: '*/*',
          'Accept-Encoding': 'gzip, deflate, br',
          'Access-Control-Allow-Origin': '*',
        },
      })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          setCurso(data.Cursos);
        });

    } catch (err) {
    } finally {
    }
  };

  return (

    <div className="h3">
      Asistencia Docente
      <br />
      <form id="miFormulario"  >
        <div className="row" style={{ marginTop: 20 }}>
          <div className="col-6">
            <input className="form-control form-control-lg text-center" id="nombre" type="text" placeholder="Digite Los Nombres Del Docente" required />
          </div>

          <div className="col-6">
            <input className="form-control form-control-lg text-center" id="apellido" type="text" placeholder="Digite Los Apellidos Del Docente" required />
          </div>
        </div>

        <div className="row" style={{ marginTop: 20 }}>
          <div className="col">
            <button className="btn btn-primary btn-lg" onClick={handleClick}>Consulta</button>
          </div>
        </div>
      </form>

      <div className="table-responsive">
        
        {
          curso.map((value,key)=>{
            return (
        <div key={key} className="row row-cols-8 row-cols-md-11 g-2" style={{ padding: 5, width: "90%", margin: "0 auto" }}>
          <div className="col">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Curso</h5>
                <p className="card-text"> {value.programacion.consecprogra} </p>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Espacio</h5>
                <p className="card-text"> {value.programacion.espacio.nomespacio} </p>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Deporte</h5>
                <p className="card-text">{value.programacion.deporte.nomdeporte} </p>
              </div>
            </div>
          </div>
          <div className="col">
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Numero de estudiantes</h5>
                <p className="card-text"> {value.programacion.noinscrito}/{value.programacion.cupo} </p>
              </div>
            </div>
          </div>
        </div>
            )
          })
        }
      </div>
    </div>
  )
}
