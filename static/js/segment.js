function validation()
{
	var age = document.getElementById('age').value;
	var family_size = document.getElementById('family_size').value;
	if(age == "" || family_size == ""){
		alert('please fill age or family size');
		return false;


	}

}
