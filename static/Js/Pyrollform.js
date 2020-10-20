$("[Full_Name='Employee']").change(function(){
   window.location(`http://127.0.0.1:8000/add_payrollform/${user.id}`);
});