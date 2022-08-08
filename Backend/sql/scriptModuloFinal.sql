/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     7/08/2022 8:05:46 p. m.                      */
/*==============================================================*/


alter table ASISMIEMBROEQUIPO
   drop constraint FK_ASISMIEM_RELACION__MIEMBROE;

alter table ASISMIEMBROEQUIPO
   drop constraint FK_ASISMIEM_RELACION__PROGRAMA;

alter table ASISTIRRESPONSABLE
   drop constraint FK_ASISTIRR_RELACION__RESPONSA;

alter table DEPORTE_TIPOELEMENTO
   drop constraint FK_DEPORTE__DEPORTE_D_DEPORTE;

alter table DEPORTE_TIPOELEMENTO
   drop constraint FK_DEPORTE__TIPOELEME_TIPOELEM;

alter table ELEMENDEPORTIVO
   drop constraint FK_ELEMENDE_RELACION__ESPACIO;

alter table ELEMENDEPORTIVO
   drop constraint FK_ELEMENDE_RELACION__ESTADO;

alter table ELEMENDEPORTIVO
   drop constraint FK_ELEMENDE_RELACION__MARCA;

alter table ELEMENDEPORTIVO
   drop constraint FK_ELEMENDE_RELACION__TIPOELEM;

alter table EMPLEADO_CARGO
   drop constraint FK_EMPLEADO_RELACION__CARGO;

alter table EMPLEADO_CARGO
   drop constraint FK_EMPLEADO_RELACION__EMPLEADO;

alter table EMPLEADO_CARGO
   drop constraint FK_EMPLEADO_RELACION__ESPACIO;

alter table EQUIPO
   drop constraint FK_EQUIPO_RELACION__DEPORTE;

alter table EQUIPO
   drop constraint FK_EQUIPO_RELACION__EMPLEADO;

alter table ESPACIO
   drop constraint FK_ESPACIO_RELACION__ESPACIO;

alter table ESPACIO
   drop constraint FK_ESPACIO_RELACION__TIPOESPA;

alter table ESPACIO_DEPORTE
   drop constraint FK_ESPACIO__DEPORTE_E_DEPORTE;

alter table ESPACIO_DEPORTE
   drop constraint FK_ESPACIO__ESPACIO_E_ESPACIO;

alter table ESTUDIANTE
   drop constraint FK_ESTUDIAN_RELACION__ESPACIO;

alter table INSCRITOPRACLIBRE
   drop constraint FK_INSCRITO_RELACION__EMPLEADO;

alter table INSCRITOPRACLIBRE
   drop constraint FK_INSCRITO_RELACION__ESTUDIAN;

alter table INSCRITOPRACLIBRE
   drop constraint FK_INSCRITO_RELACION__PROGRAMA;

alter table MIEMBROEQUIPO
   drop constraint FK_MIEMBROE_RELACION__EQUIPO;

alter table MIEMBROEQUIPO
   drop constraint FK_MIEMBROE_RELACION__ESTUDIAN;

alter table PRESTAMO
   drop constraint FK_PRESTAMO_RELACION__ASISTIRR;

alter table PRESTAMO
   drop constraint FK_PRESTAMO_RELACION__ELEMENDE;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_HORAFIN_P_HORA;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_HORAINICI_HORA;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_RELACION__ACTIVIDA;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_RELACION__DEPORTE;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_RELACION__DIA;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_RELACION__ESPACIO;

alter table PROGRAMACION
   drop constraint FK_PROGRAMA_RELACION__PERIODO;

alter table RESPONSABLE
   drop constraint FK_RESPONSA_RELACION__EMPLEADO;

alter table RESPONSABLE
   drop constraint FK_RESPONSA_RELACION__ESTUDIAN;

alter table RESPONSABLE
   drop constraint FK_RESPONSA_RELACION__PROGRAMA;

alter table RESPONSABLE
   drop constraint FK_RESPONSA_RELACION__ROL;

drop table ACTIVIDAD cascade constraints;

drop index PROGRAMACION_ASISMIEMEQ_FK;

drop index MIEMBROEQUIPO_ASISMIEMEQ_FK;

drop table ASISMIEMBROEQUIPO cascade constraints;

drop index RESPONSABLE_ASISRESP_FK;

drop table ASISTIRRESPONSABLE cascade constraints;

drop table CARGO cascade constraints;

drop table DEPORTE cascade constraints;

drop index DEPORTE_TIPOELEMENTO_FK;

drop index DEPORTE_TIPOELEMENTO2_FK;

drop table DEPORTE_TIPOELEMENTO cascade constraints;

drop table DIA cascade constraints;

drop index MARCA_ELEMENDEPORTIVO_FK;

drop index ESTADO_ELEMENDEPORTIVO_FK;

drop index TIPOELEMENTO_ELEDEP_FK;

drop index ESPACIO_ELEMENDEPORTIVO_FK;

drop table ELEMENDEPORTIVO cascade constraints;

drop table EMPLEADO cascade constraints;

drop index EMPLEADO_EMPLEADO_CARGO_FK;

drop index CARGO_EMPLEADO_CARGO_FK;

drop index ESPACIO_EMPLEADO_CARGO_FK;

drop table EMPLEADO_CARGO cascade constraints;

drop index RELACION_EMPLEADO_EQUIPO_FK;

drop index RELACION_DEPORTE_EQUIPO_FK;

drop table EQUIPO cascade constraints;

drop index RELACION_ESPACIO_ESPACIO_FK;

drop index TIPOESPACIO_ESPACIO_FK;

drop table ESPACIO cascade constraints;

drop index RELACION_ESPACIO_DEPORTE_FK;

drop index RELACION_ESPACIO_DEPORTE2_FK;

drop table ESPACIO_DEPORTE cascade constraints;

drop table ESTADO cascade constraints;

drop index RELACION_ESPACIO_ESTUDIANTE_FK;

drop table ESTUDIANTE cascade constraints;

drop table HORA cascade constraints;

drop index PROGRAMACION_INSPRACLIB_FK;

drop index ESTUDIANTE_INSPRACLIB_FK;

drop index EMPLEADO_INSCRITOPRACLIBRE_FK;

drop table INSCRITOPRACLIBRE cascade constraints;

drop table MARCA cascade constraints;

drop index EQUIPO_MIEMBROEQUIPO_FK;

drop index ESTUDIANTE_MIEMBROEQUIPO_FK;

drop table MIEMBROEQUIPO cascade constraints;

drop table PERIODO cascade constraints;

drop index ELEMENDEPORTIVO_PRESTAMO_FK;

drop index ASISTIRRESPONSABLE_PRESTAMO_FK;

drop table PRESTAMO cascade constraints;

drop index RELACION_DIA_PROGRAMACION_FK;

drop index HORAINICIO_PROGRAMACION_FK;

drop index HORAFIN_PROGRAMACION_FK;

drop index ACTIVIDAD_PROGRAMACION_FK;

drop index PERIODO_PROGRAMACION_FK;

drop index DEPORTE_PROGRAMACION_FK;

drop index ESPACIO_PROGRAMACION_FK;

drop table PROGRAMACION cascade constraints;

drop index PROGRAMACION_RESPONSABLE_FK;

drop index RELACION_ROL_RESPONSABLE_FK;

drop index ESTUDIANTE_RESPONSABLE_FK;

drop index EMPLEADO_RESPONSABLE_FK;

drop table RESPONSABLE cascade constraints;

drop table ROL cascade constraints;

drop table TIPOELEMENTO cascade constraints;

drop table TIPOESPACIO cascade constraints;

/*==============================================================*/
/* Table: ACTIVIDAD                                             */
/*==============================================================*/
create table ACTIVIDAD 
(
   IDACTIVIDAD          VARCHAR2(2)          not null,
   DESCACTIVIDAD        VARCHAR2(30)         not null,
   constraint PK_ACTIVIDAD primary key (IDACTIVIDAD)
);

/*==============================================================*/
/* Table: ASISMIEMBROEQUIPO                                     */
/*==============================================================*/
create table ASISMIEMBROEQUIPO 
(
   CONSECPROGRA_ASISMIEMBROEQUIPO NUMBER(4,0)          not null,
   CONMIEMEQUIPO        NUMBER(4,0)          not null,
   CONSEEQUIPO_MIEMEQ_ASISMIEMEQ NUMBER(3,0)          not null,
   ITEMMIEMBRO_ASISMIEMBROEQUIPO NUMBER(3,0)          not null,
   constraint PK_ASISMIEMBROEQUIPO primary key (CONSECPROGRA_ASISMIEMBROEQUIPO, CONMIEMEQUIPO)
);

/*==============================================================*/
/* Index: MIEMBROEQUIPO_ASISMIEMEQ_FK                           */
/*==============================================================*/
create index MIEMBROEQUIPO_ASISMIEMEQ_FK on ASISMIEMBROEQUIPO (
   CONSEEQUIPO_MIEMEQ_ASISMIEMEQ ASC,
   ITEMMIEMBRO_ASISMIEMBROEQUIPO ASC
);

/*==============================================================*/
/* Index: PROGRAMACION_ASISMIEMEQ_FK                            */
/*==============================================================*/
create index PROGRAMACION_ASISMIEMEQ_FK on ASISMIEMBROEQUIPO (
   CONSECPROGRA_ASISMIEMBROEQUIPO ASC
);

/*==============================================================*/
/* Table: ASISTIRRESPONSABLE                                    */
/*==============================================================*/
create table ASISTIRRESPONSABLE 
(
   CONSECPROGRA_RESPONSABLE NUMBER(4,0)          not null,
   CONSECRES_ASISTIRRESPONSABLE NUMBER(4,0)          not null,
   CONSECASISRES        NUMBER(4,0)          not null,
   FECHAASISRES         DATE                 not null,
   HORAASISRES          DATE                 not null,
   constraint PK_ASISTIRRESPONSABLE primary key (CONSECPROGRA_RESPONSABLE, CONSECRES_ASISTIRRESPONSABLE, CONSECASISRES)
);

/*==============================================================*/
/* Index: RESPONSABLE_ASISRESP_FK                               */
/*==============================================================*/
create index RESPONSABLE_ASISRESP_FK on ASISTIRRESPONSABLE (
   CONSECPROGRA_RESPONSABLE ASC,
   CONSECRES_ASISTIRRESPONSABLE ASC
);

/*==============================================================*/
/* Table: CARGO                                                 */
/*==============================================================*/
create table CARGO 
(
   IDCARGO              VARCHAR2(2)          not null,
   DESCARGO             VARCHAR2(20)         not null,
   constraint PK_CARGO primary key (IDCARGO)
);

/*==============================================================*/
/* Table: DEPORTE                                               */
/*==============================================================*/
create table DEPORTE 
(
   IDDEPORTE            VARCHAR2(2)          not null,
   NOMDEPORTE           VARCHAR2(20)         not null,
   constraint PK_DEPORTE primary key (IDDEPORTE)
);

/*==============================================================*/
/* Table: DEPORTE_TIPOELEMENTO                                  */
/*==============================================================*/
create table DEPORTE_TIPOELEMENTO 
(
   IDTIPOELEMENTO_DEPORTIPOELE VARCHAR2(2)          not null,
   IDDEPORTE_DEPORTETIPOELEMENTO VARCHAR2(2)          not null,
   constraint PK_DEPORTE_TIPOELEMENTO primary key (IDTIPOELEMENTO_DEPORTIPOELE, IDDEPORTE_DEPORTETIPOELEMENTO)
);

/*==============================================================*/
/* Index: DEPORTE_TIPOELEMENTO2_FK                              */
/*==============================================================*/
create index DEPORTE_TIPOELEMENTO2_FK on DEPORTE_TIPOELEMENTO (
   IDDEPORTE_DEPORTETIPOELEMENTO ASC
);

/*==============================================================*/
/* Index: DEPORTE_TIPOELEMENTO_FK                               */
/*==============================================================*/
create index DEPORTE_TIPOELEMENTO_FK on DEPORTE_TIPOELEMENTO (
   IDTIPOELEMENTO_DEPORTIPOELE ASC
);

/*==============================================================*/
/* Table: DIA                                                   */
/*==============================================================*/
create table DIA 
(
   IDDIA                VARCHAR2(2)          not null,
   NOMDIA               VARCHAR2(10)         not null,
   constraint PK_DIA primary key (IDDIA)
);

/*==============================================================*/
/* Table: ELEMENDEPORTIVO                                       */
/*==============================================================*/
create table ELEMENDEPORTIVO 
(
   CONSECELEMENTO       NUMBER(5,0)          not null,
   CODESPACIO_ELEMENDEPORTIVO VARCHAR2(2)          not null,
   IDTIPOELEMENTO_ELEMENDEPORTIVO VARCHAR2(2)          not null,
   IDESTADO_ELEMENDEPORTIVO VARCHAR2(2)          not null,
   IDMARCA_ELEMENDEPORTIVO VARCHAR2(2)          not null,
   FECHAREGISTRO        DATE                 not null,
   constraint PK_ELEMENDEPORTIVO primary key (CONSECELEMENTO)
);

/*==============================================================*/
/* Index: ESPACIO_ELEMENDEPORTIVO_FK                            */
/*==============================================================*/
create index ESPACIO_ELEMENDEPORTIVO_FK on ELEMENDEPORTIVO (
   CODESPACIO_ELEMENDEPORTIVO ASC
);

/*==============================================================*/
/* Index: TIPOELEMENTO_ELEDEP_FK                                */
/*==============================================================*/
create index TIPOELEMENTO_ELEDEP_FK on ELEMENDEPORTIVO (
   IDTIPOELEMENTO_ELEMENDEPORTIVO ASC
);

/*==============================================================*/
/* Index: ESTADO_ELEMENDEPORTIVO_FK                             */
/*==============================================================*/
create index ESTADO_ELEMENDEPORTIVO_FK on ELEMENDEPORTIVO (
   IDESTADO_ELEMENDEPORTIVO ASC
);

/*==============================================================*/
/* Index: MARCA_ELEMENDEPORTIVO_FK                              */
/*==============================================================*/
create index MARCA_ELEMENDEPORTIVO_FK on ELEMENDEPORTIVO (
   IDMARCA_ELEMENDEPORTIVO ASC
);

/*==============================================================*/
/* Table: EMPLEADO                                              */
/*==============================================================*/
create table EMPLEADO 
(
   CODEMPLEADO          VARCHAR2(4)          not null,
   NOMEMPLEADO          VARCHAR2(20)         not null,
   APELLEMPLEADO        VARCHAR2(20)         not null,
   FECHAREGISTRO        DATE                 not null,
   CORREOUD             VARCHAR2(30)         not null,
   constraint PK_EMPLEADO primary key (CODEMPLEADO)
);

/*==============================================================*/
/* Table: EMPLEADO_CARGO                                        */
/*==============================================================*/
create table EMPLEADO_CARGO 
(
   CONSEC               NUMBER(3,0)          not null,
   CODESPACIO_EMPLEADOCARGO VARCHAR2(2)          not null,
   IDCARGO_EMPLEADOCARGO VARCHAR2(2)          not null,
   CODEMPLEADO_EMPLEADOCARGO VARCHAR2(4)          not null,
   FECHACARGO           DATE                 not null,
   FECHAFINCAR          DATE,
   constraint PK_EMPLEADO_CARGO primary key (CONSEC)
);

/*==============================================================*/
/* Index: ESPACIO_EMPLEADO_CARGO_FK                             */
/*==============================================================*/
create index ESPACIO_EMPLEADO_CARGO_FK on EMPLEADO_CARGO (
   CODESPACIO_EMPLEADOCARGO ASC
);

/*==============================================================*/
/* Index: CARGO_EMPLEADO_CARGO_FK                               */
/*==============================================================*/
create index CARGO_EMPLEADO_CARGO_FK on EMPLEADO_CARGO (
   IDCARGO_EMPLEADOCARGO ASC
);

/*==============================================================*/
/* Index: EMPLEADO_EMPLEADO_CARGO_FK                            */
/*==============================================================*/
create index EMPLEADO_EMPLEADO_CARGO_FK on EMPLEADO_CARGO (
   CODEMPLEADO_EMPLEADOCARGO ASC
);

/*==============================================================*/
/* Table: EQUIPO                                                */
/*==============================================================*/
create table EQUIPO 
(
   CONSEEQUIPO          NUMBER(3,0)          not null,
   IDDEPORTE_EQUIPO     VARCHAR2(2)          not null,
   CODEMPLEADO_EQUIPO   VARCHAR2(4)          not null,
   FECHARESOL           DATE                 not null,
   constraint PK_EQUIPO primary key (CONSEEQUIPO)
);

/*==============================================================*/
/* Index: RELACION_DEPORTE_EQUIPO_FK                            */
/*==============================================================*/
create index RELACION_DEPORTE_EQUIPO_FK on EQUIPO (
   IDDEPORTE_EQUIPO ASC
);

/*==============================================================*/
/* Index: RELACION_EMPLEADO_EQUIPO_FK                           */
/*==============================================================*/
create index RELACION_EMPLEADO_EQUIPO_FK on EQUIPO (
   CODEMPLEADO_EQUIPO ASC
);

/*==============================================================*/
/* Table: ESPACIO                                               */
/*==============================================================*/
create table ESPACIO 
(
   CODESPACIO           VARCHAR2(2)          not null,
   IDTIPOESPACIO_ESPACIO VARCHAR2(2)          not null,
   CODESPACIO_ESPACIO   VARCHAR2(2),
   NOMESPACIO           VARCHAR2(30)         not null,
   constraint PK_ESPACIO primary key (CODESPACIO)
);

/*==============================================================*/
/* Index: TIPOESPACIO_ESPACIO_FK                                */
/*==============================================================*/
create index TIPOESPACIO_ESPACIO_FK on ESPACIO (
   IDTIPOESPACIO_ESPACIO ASC
);

/*==============================================================*/
/* Index: RELACION_ESPACIO_ESPACIO_FK                           */
/*==============================================================*/
create index RELACION_ESPACIO_ESPACIO_FK on ESPACIO (
   CODESPACIO_ESPACIO ASC
);

/*==============================================================*/
/* Table: ESPACIO_DEPORTE                                       */
/*==============================================================*/
create table ESPACIO_DEPORTE 
(
   CODESPACIO_ESPACIODEPORTE VARCHAR2(2)          not null,
   IDDEPORTE_ESPACIODEPORTE VARCHAR2(2)          not null,
   constraint PK_ESPACIO_DEPORTE primary key (CODESPACIO_ESPACIODEPORTE, IDDEPORTE_ESPACIODEPORTE)
);

/*==============================================================*/
/* Index: RELACION_ESPACIO_DEPORTE2_FK                          */
/*==============================================================*/
create index RELACION_ESPACIO_DEPORTE2_FK on ESPACIO_DEPORTE (
   IDDEPORTE_ESPACIODEPORTE ASC
);

/*==============================================================*/
/* Index: RELACION_ESPACIO_DEPORTE_FK                           */
/*==============================================================*/
create index RELACION_ESPACIO_DEPORTE_FK on ESPACIO_DEPORTE (
   CODESPACIO_ESPACIODEPORTE ASC
);

/*==============================================================*/
/* Table: ESTADO                                                */
/*==============================================================*/
create table ESTADO 
(
   IDESTADO             VARCHAR2(2)          not null,
   DESCESTADO           VARCHAR2(20)         not null,
   constraint PK_ESTADO primary key (IDESTADO)
);

/*==============================================================*/
/* Table: ESTUDIANTE                                            */
/*==============================================================*/
create table ESTUDIANTE 
(
   CODESTU              VARCHAR2(12)         not null,
   CODESPACIO_ESTUDIANTE VARCHAR2(2)          not null,
   NOMESTU              VARCHAR2(30)         not null,
   APELESTU             VARCHAR2(30)         not null,
   FECHAREGESTU         DATE                 not null,
   CORREOUDESTU         VARCHAR2(30)         not null,
   FECHANACESTU         DATE                 not null,
   constraint PK_ESTUDIANTE primary key (CODESTU)
);

/*==============================================================*/
/* Index: RELACION_ESPACIO_ESTUDIANTE_FK                        */
/*==============================================================*/
create index RELACION_ESPACIO_ESTUDIANTE_FK on ESTUDIANTE (
   CODESPACIO_ESTUDIANTE ASC
);

/*==============================================================*/
/* Table: HORA                                                  */
/*==============================================================*/
create table HORA 
(
   IDHORA               VARCHAR2(2)          not null,
   constraint PK_HORA primary key (IDHORA)
);

/*==============================================================*/
/* Table: INSCRITOPRACLIBRE                                     */
/*==============================================================*/
create table INSCRITOPRACLIBRE 
(
   CONSECPROGRA_INSCRITOPRACLIBRE NUMBER(4,0)          not null,
   CONSECPRACT          NUMBER(4,0)          not null,
   CODEMPLEADO_INSCRITOPRACLIBRE VARCHAR2(4),
   CODESTU_INSCRITOPRACLIBRE VARCHAR2(12),
   constraint PK_INSCRITOPRACLIBRE primary key (CONSECPROGRA_INSCRITOPRACLIBRE, CONSECPRACT)
);

/*==============================================================*/
/* Index: EMPLEADO_INSCRITOPRACLIBRE_FK                         */
/*==============================================================*/
create index EMPLEADO_INSCRITOPRACLIBRE_FK on INSCRITOPRACLIBRE (
   CODEMPLEADO_INSCRITOPRACLIBRE ASC
);

/*==============================================================*/
/* Index: ESTUDIANTE_INSPRACLIB_FK                              */
/*==============================================================*/
create index ESTUDIANTE_INSPRACLIB_FK on INSCRITOPRACLIBRE (
   CODESTU_INSCRITOPRACLIBRE ASC
);

/*==============================================================*/
/* Index: PROGRAMACION_INSPRACLIB_FK                            */
/*==============================================================*/
create index PROGRAMACION_INSPRACLIB_FK on INSCRITOPRACLIBRE (
   CONSECPROGRA_INSCRITOPRACLIBRE ASC
);

/*==============================================================*/
/* Table: MARCA                                                 */
/*==============================================================*/
create table MARCA 
(
   IDMARCA              VARCHAR2(2)          not null,
   NOMMARCA             VARCHAR2(20)         not null,
   constraint PK_MARCA primary key (IDMARCA)
);

/*==============================================================*/
/* Table: MIEMBROEQUIPO                                         */
/*==============================================================*/
create table MIEMBROEQUIPO 
(
   CONSEEQUIPO_MIEMBROEQUIPO NUMBER(3,0)          not null,
   ITEMMIEMBRO          NUMBER(3,0)          not null,
   CODESTU_MIEMBROEQUIPO VARCHAR2(12)         not null,
   constraint PK_MIEMBROEQUIPO primary key (CONSEEQUIPO_MIEMBROEQUIPO, ITEMMIEMBRO)
);

/*==============================================================*/
/* Index: ESTUDIANTE_MIEMBROEQUIPO_FK                           */
/*==============================================================*/
create index ESTUDIANTE_MIEMBROEQUIPO_FK on MIEMBROEQUIPO (
   CODESTU_MIEMBROEQUIPO ASC
);

/*==============================================================*/
/* Index: EQUIPO_MIEMBROEQUIPO_FK                               */
/*==============================================================*/
create index EQUIPO_MIEMBROEQUIPO_FK on MIEMBROEQUIPO (
   CONSEEQUIPO_MIEMBROEQUIPO ASC
);

/*==============================================================*/
/* Table: PERIODO                                               */
/*==============================================================*/
create table PERIODO 
(
   IDPERIODO            VARCHAR2(5)          not null,
   constraint PK_PERIODO primary key (IDPERIODO)
);

/*==============================================================*/
/* Table: PRESTAMO                                              */
/*==============================================================*/
create table PRESTAMO 
(
   CONSECPRESTAMO       NUMBER(4,0)          not null,
   CONSECPROGRA_RESP_PREST NUMBER(4,0)          not null,
   CONSECRES_ASISRESP_PREST NUMBER(4,0)          not null,
   CONSECASISRES_PRESTAMO NUMBER(4,0)          not null,
   CONSECELEMENTO_PRESTAMO NUMBER(5,0)          not null,
   constraint PK_PRESTAMO primary key (CONSECPRESTAMO)
);

/*==============================================================*/
/* Index: ASISTIRRESPONSABLE_PRESTAMO_FK                        */
/*==============================================================*/
create index ASISTIRRESPONSABLE_PRESTAMO_FK on PRESTAMO (
   CONSECPROGRA_RESP_PREST ASC,
   CONSECRES_ASISRESP_PREST ASC,
   CONSECASISRES_PRESTAMO ASC
);

/*==============================================================*/
/* Index: ELEMENDEPORTIVO_PRESTAMO_FK                           */
/*==============================================================*/
create index ELEMENDEPORTIVO_PRESTAMO_FK on PRESTAMO (
   CONSECELEMENTO_PRESTAMO ASC
);

/*==============================================================*/
/* Table: PROGRAMACION                                          */
/*==============================================================*/
create table PROGRAMACION 
(
   CONSECPROGRA         NUMBER(4,0)          not null,
   CODESPACIO_PROGRAMACION VARCHAR2(2),
   IDDEPORTE_PROGRAMACION VARCHAR2(2)          not null,
   IDPERIODO_PROGRAMACION VARCHAR2(5)          not null,
   IDACTIVIDAD_PROGRAMACION VARCHAR2(2)          not null,
   IDHORAINICIO_PROGRAMACION VARCHAR2(2)          not null,
   IDHORAFIN_PROGRAMACION VARCHAR2(2)          not null,
   IDDIA_PROGRAMACION   VARCHAR2(2)          not null,
   CUPO                 NUMBER(3,0)          not null,
   NOINSCRITO           NUMBER(3,0)          not null,
   constraint PK_PROGRAMACION primary key (CONSECPROGRA)
);

/*==============================================================*/
/* Index: ESPACIO_PROGRAMACION_FK                               */
/*==============================================================*/
create index ESPACIO_PROGRAMACION_FK on PROGRAMACION (
   CODESPACIO_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: DEPORTE_PROGRAMACION_FK                               */
/*==============================================================*/
create index DEPORTE_PROGRAMACION_FK on PROGRAMACION (
   IDDEPORTE_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: PERIODO_PROGRAMACION_FK                               */
/*==============================================================*/
create index PERIODO_PROGRAMACION_FK on PROGRAMACION (
   IDPERIODO_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: ACTIVIDAD_PROGRAMACION_FK                             */
/*==============================================================*/
create index ACTIVIDAD_PROGRAMACION_FK on PROGRAMACION (
   IDACTIVIDAD_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: HORAFIN_PROGRAMACION_FK                               */
/*==============================================================*/
create index HORAFIN_PROGRAMACION_FK on PROGRAMACION (
   IDHORAINICIO_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: HORAINICIO_PROGRAMACION_FK                            */
/*==============================================================*/
create index HORAINICIO_PROGRAMACION_FK on PROGRAMACION (
   IDHORAFIN_PROGRAMACION ASC
);

/*==============================================================*/
/* Index: RELACION_DIA_PROGRAMACION_FK                          */
/*==============================================================*/
create index RELACION_DIA_PROGRAMACION_FK on PROGRAMACION (
   IDDIA_PROGRAMACION ASC
);

/*==============================================================*/
/* Table: RESPONSABLE                                           */
/*==============================================================*/
create table RESPONSABLE 
(
   CONSECPROGRA_RESPONSABLE NUMBER(4,0)          not null,
   CONSECRES            NUMBER(4,0)          not null,
   CODEMPLEADO_RESPONSABLE VARCHAR2(4)          not null,
   CODESTU_RESPONSABLE  VARCHAR2(12),
   IDROL_RESPONSABLE    VARCHAR2(1),
   FECHAINI             DATE                 not null,
   FECHAFIN             DATE                 not null,
   constraint PK_RESPONSABLE primary key (CONSECPROGRA_RESPONSABLE, CONSECRES)
);

/*==============================================================*/
/* Index: EMPLEADO_RESPONSABLE_FK                               */
/*==============================================================*/
create index EMPLEADO_RESPONSABLE_FK on RESPONSABLE (
   CODEMPLEADO_RESPONSABLE ASC
);

/*==============================================================*/
/* Index: ESTUDIANTE_RESPONSABLE_FK                             */
/*==============================================================*/
create index ESTUDIANTE_RESPONSABLE_FK on RESPONSABLE (
   CODESTU_RESPONSABLE ASC
);

/*==============================================================*/
/* Index: RELACION_ROL_RESPONSABLE_FK                           */
/*==============================================================*/
create index RELACION_ROL_RESPONSABLE_FK on RESPONSABLE (
   IDROL_RESPONSABLE ASC
);

/*==============================================================*/
/* Index: PROGRAMACION_RESPONSABLE_FK                           */
/*==============================================================*/
create index PROGRAMACION_RESPONSABLE_FK on RESPONSABLE (
   CONSECPROGRA_RESPONSABLE ASC
);

/*==============================================================*/
/* Table: ROL                                                   */
/*==============================================================*/
create table ROL 
(
   IDROL                VARCHAR2(1)          not null,
   DESCROL              VARCHAR2(15)         not null,
   constraint PK_ROL primary key (IDROL)
);

/*==============================================================*/
/* Table: TIPOELEMENTO                                          */
/*==============================================================*/
create table TIPOELEMENTO 
(
   IDTIPOELEMENTO       VARCHAR2(2)          not null,
   DESCTIPOELEMENTO     VARCHAR2(40)         not null,
   constraint PK_TIPOELEMENTO primary key (IDTIPOELEMENTO)
);

/*==============================================================*/
/* Table: TIPOESPACIO                                           */
/*==============================================================*/
create table TIPOESPACIO 
(
   IDTIPOESPACIO        VARCHAR2(2)          not null,
   DESCTIPOESPACIO      VARCHAR2(30)         not null,
   constraint PK_TIPOESPACIO primary key (IDTIPOESPACIO)
);

alter table ASISMIEMBROEQUIPO
   add constraint FK_ASISMIEM_RELACION__MIEMBROE foreign key (CONSEEQUIPO_MIEMEQ_ASISMIEMEQ, ITEMMIEMBRO_ASISMIEMBROEQUIPO)
      references MIEMBROEQUIPO (CONSEEQUIPO_MIEMBROEQUIPO, ITEMMIEMBRO);

alter table ASISMIEMBROEQUIPO
   add constraint FK_ASISMIEM_RELACION__PROGRAMA foreign key (CONSECPROGRA_ASISMIEMBROEQUIPO)
      references PROGRAMACION (CONSECPROGRA);

alter table ASISTIRRESPONSABLE
   add constraint FK_ASISTIRR_RELACION__RESPONSA foreign key (CONSECPROGRA_RESPONSABLE, CONSECRES_ASISTIRRESPONSABLE)
      references RESPONSABLE (CONSECPROGRA_RESPONSABLE, CONSECRES);

alter table DEPORTE_TIPOELEMENTO
   add constraint FK_DEPORTE__DEPORTE_D_DEPORTE foreign key (IDDEPORTE_DEPORTETIPOELEMENTO)
      references DEPORTE (IDDEPORTE);

alter table DEPORTE_TIPOELEMENTO
   add constraint FK_DEPORTE__TIPOELEME_TIPOELEM foreign key (IDTIPOELEMENTO_DEPORTIPOELE)
      references TIPOELEMENTO (IDTIPOELEMENTO);

alter table ELEMENDEPORTIVO
   add constraint FK_ELEMENDE_RELACION__ESPACIO foreign key (CODESPACIO_ELEMENDEPORTIVO)
      references ESPACIO (CODESPACIO);

alter table ELEMENDEPORTIVO
   add constraint FK_ELEMENDE_RELACION__ESTADO foreign key (IDESTADO_ELEMENDEPORTIVO)
      references ESTADO (IDESTADO);

alter table ELEMENDEPORTIVO
   add constraint FK_ELEMENDE_RELACION__MARCA foreign key (IDMARCA_ELEMENDEPORTIVO)
      references MARCA (IDMARCA);

alter table ELEMENDEPORTIVO
   add constraint FK_ELEMENDE_RELACION__TIPOELEM foreign key (IDTIPOELEMENTO_ELEMENDEPORTIVO)
      references TIPOELEMENTO (IDTIPOELEMENTO);

alter table EMPLEADO_CARGO
   add constraint FK_EMPLEADO_RELACION__CARGO foreign key (IDCARGO_EMPLEADOCARGO)
      references CARGO (IDCARGO);

alter table EMPLEADO_CARGO
   add constraint FK_EMPLEADO_RELACION__EMPLEADO foreign key (CODEMPLEADO_EMPLEADOCARGO)
      references EMPLEADO (CODEMPLEADO);

alter table EMPLEADO_CARGO
   add constraint FK_EMPLEADO_RELACION__ESPACIO foreign key (CODESPACIO_EMPLEADOCARGO)
      references ESPACIO (CODESPACIO);

alter table EQUIPO
   add constraint FK_EQUIPO_RELACION__DEPORTE foreign key (IDDEPORTE_EQUIPO)
      references DEPORTE (IDDEPORTE);

alter table EQUIPO
   add constraint FK_EQUIPO_RELACION__EMPLEADO foreign key (CODEMPLEADO_EQUIPO)
      references EMPLEADO (CODEMPLEADO);

alter table ESPACIO
   add constraint FK_ESPACIO_RELACION__ESPACIO foreign key (CODESPACIO_ESPACIO)
      references ESPACIO (CODESPACIO);

alter table ESPACIO
   add constraint FK_ESPACIO_RELACION__TIPOESPA foreign key (IDTIPOESPACIO_ESPACIO)
      references TIPOESPACIO (IDTIPOESPACIO);

alter table ESPACIO_DEPORTE
   add constraint FK_ESPACIO__DEPORTE_E_DEPORTE foreign key (IDDEPORTE_ESPACIODEPORTE)
      references DEPORTE (IDDEPORTE);

alter table ESPACIO_DEPORTE
   add constraint FK_ESPACIO__ESPACIO_E_ESPACIO foreign key (CODESPACIO_ESPACIODEPORTE)
      references ESPACIO (CODESPACIO);

alter table ESTUDIANTE
   add constraint FK_ESTUDIAN_RELACION__ESPACIO foreign key (CODESPACIO_ESTUDIANTE)
      references ESPACIO (CODESPACIO);

alter table INSCRITOPRACLIBRE
   add constraint FK_INSCRITO_RELACION__EMPLEADO foreign key (CODEMPLEADO_INSCRITOPRACLIBRE)
      references EMPLEADO (CODEMPLEADO);

alter table INSCRITOPRACLIBRE
   add constraint FK_INSCRITO_RELACION__ESTUDIAN foreign key (CODESTU_INSCRITOPRACLIBRE)
      references ESTUDIANTE (CODESTU);

alter table INSCRITOPRACLIBRE
   add constraint FK_INSCRITO_RELACION__PROGRAMA foreign key (CONSECPROGRA_INSCRITOPRACLIBRE)
      references PROGRAMACION (CONSECPROGRA);

alter table MIEMBROEQUIPO
   add constraint FK_MIEMBROE_RELACION__EQUIPO foreign key (CONSEEQUIPO_MIEMBROEQUIPO)
      references EQUIPO (CONSEEQUIPO);

alter table MIEMBROEQUIPO
   add constraint FK_MIEMBROE_RELACION__ESTUDIAN foreign key (CODESTU_MIEMBROEQUIPO)
      references ESTUDIANTE (CODESTU);

alter table PRESTAMO
   add constraint FK_PRESTAMO_RELACION__ASISTIRR foreign key (CONSECPROGRA_RESP_PREST, CONSECRES_ASISRESP_PREST, CONSECASISRES_PRESTAMO)
      references ASISTIRRESPONSABLE (CONSECPROGRA_RESPONSABLE, CONSECRES_ASISTIRRESPONSABLE, CONSECASISRES);

alter table PRESTAMO
   add constraint FK_PRESTAMO_RELACION__ELEMENDE foreign key (CONSECELEMENTO_PRESTAMO)
      references ELEMENDEPORTIVO (CONSECELEMENTO);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_HORAFIN_P_HORA foreign key (IDHORAINICIO_PROGRAMACION)
      references HORA (IDHORA);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_HORAINICI_HORA foreign key (IDHORAFIN_PROGRAMACION)
      references HORA (IDHORA);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_RELACION__ACTIVIDA foreign key (IDACTIVIDAD_PROGRAMACION)
      references ACTIVIDAD (IDACTIVIDAD);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_RELACION__DEPORTE foreign key (IDDEPORTE_PROGRAMACION)
      references DEPORTE (IDDEPORTE);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_RELACION__DIA foreign key (IDDIA_PROGRAMACION)
      references DIA (IDDIA);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_RELACION__ESPACIO foreign key (CODESPACIO_PROGRAMACION)
      references ESPACIO (CODESPACIO);

alter table PROGRAMACION
   add constraint FK_PROGRAMA_RELACION__PERIODO foreign key (IDPERIODO_PROGRAMACION)
      references PERIODO (IDPERIODO);

alter table RESPONSABLE
   add constraint FK_RESPONSA_RELACION__EMPLEADO foreign key (CODEMPLEADO_RESPONSABLE)
      references EMPLEADO (CODEMPLEADO);

alter table RESPONSABLE
   add constraint FK_RESPONSA_RELACION__ESTUDIAN foreign key (CODESTU_RESPONSABLE)
      references ESTUDIANTE (CODESTU);

alter table RESPONSABLE
   add constraint FK_RESPONSA_RELACION__PROGRAMA foreign key (CONSECPROGRA_RESPONSABLE)
      references PROGRAMACION (CONSECPROGRA);

alter table RESPONSABLE
   add constraint FK_RESPONSA_RELACION__ROL foreign key (IDROL_RESPONSABLE)
      references ROL (IDROL);

