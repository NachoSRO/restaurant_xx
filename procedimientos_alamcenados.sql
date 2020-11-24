create or replace procedure sp_lisar_productos(productos out SYS_REFCURSOR)
is

begin

    open productos for select * from producto;
end;

create or replace procedure sp_agregar_producto(
    v_nombre varchar2,
    v_cod_producto varchar2,
    v_cantidad number,
    v_descripcion varchar2,
    v_salida out number
)is
begin
    insert into producto(name,cod_producto,cantidad,descripcion)
    values(v_nombre,v_cod_producto,v_cantidad,v_descripcion);
    commit;
    v_salida:=1;

    exception

    when others then
        v_salida:=0;
end;

create or replace trigger sumar_pedido_stock
after insert or update on FACTURAPEDIDO_PROD FOR EACH ROW
declare
begin
             update producto
             set stock = stock + :new.cantidad
             where  id = :new.producto_id;

end;