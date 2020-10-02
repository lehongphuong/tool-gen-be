<?php 
	switch ($data->what) { 
        //******************importgoods************************
        // importgoods(id,idproduct,amount,dateadd,expirydate,manufacturedate,note)
        // Get all data from importgoods
        case 500: {
            $sql = "SELECT * FROM importgoods";
            break;
        }

        // Insert data to importgoods
        case 501: {
            $sql = "INSERT INTO importgoods(idproduct,amount,dateadd,expirydate,manufacturedate,note)
            		VALUES('$data->idproduct','$data->amount','$data->dateadd','$data->expirydate','$data->manufacturedate','$data->note')";
            break;
        }

        // Update data importgoods
        case 502: {
            $sql = "UPDATE importgoods SET idproduct='$data->idproduct', amount='$data->amount', dateadd='$data->dateadd', expirydate='$data->expirydate', manufacturedate='$data->manufacturedate', note = '$data->note'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of importgoods
        case 503: {
            $sql = "DELETE FROM importgoods
            		WHERE id IN($data->id)";
            break;
        }

        // Find data with id importgoods
        case 504: {
            $sql = "SELECT * FROM importgoods
            		WHERE id='$data->id'";
            break;
        }

        // Select with pagination(offset, number-item-in-page) importgoods
        case 505: {
            $sql = "SELECT * FROM importgoods
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of importgoods
        case 506: {
            $sql = "SELECT COUNT(1) FROM importgoods ";
            break;
        }

	}
?> 
