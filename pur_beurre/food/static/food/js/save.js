document.addEventListener('click', (event) =>{
    if (!event.target.classList.contains("save_food")) {
        return
    }
    event.preventDefault()
    var food_id_pk = event.target.dataset.foodId;
    console.log(food_id_pk);
    var data = { id: food_id_pk};
    ajaxPost("/ajax/", data, function(response){
        console.log("envoi réussi");
        },true);
    alert(event.target.innerHTML="Aliment ajouté à vos favoris");

});