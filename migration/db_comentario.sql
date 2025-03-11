create database db_comentarios;
use db_comentarios;

create table tb_comentarios(
	nome varchar(100) not null,
    comentario text not null,
    data_hora datetime not null,
    cod_comentario int primary key auto_increment
);