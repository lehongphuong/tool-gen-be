<?php 
	switch ($data->what) { 
        //******************city and district************************
        // staff(id, fullname, username, password, phone, email,position, permission)
        // Get all data from 
        case 600: {
            $sql = "SELECT * FROM city";
            break;
        }

        // Get all data from  
        case 601: {
            $sql = "SELECT * FROM district";
            break;
        }
		
		// get district with id company

		case 602: {

            $sql = "SELECT id, name FROM district WHERE idcity= '$data->idcity'";

            break;

        }

        

	}
?> 
