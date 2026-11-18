function leerSolicitud() {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const fila = hoja.getRange("A2:D2").getValues()[0];
  console.log(fila);
}

function actualizarEstado() {
  const hoja = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  hoja.getRange("D2").setValue("revisada");
}