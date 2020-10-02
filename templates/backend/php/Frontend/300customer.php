<?php 
	switch ($data->what) { 
        //******************customer************************
        // customer(id,name,phone,email,age,address,district,city,zalo,facebook)
        // Get all data from customer
        case 300: {
            $sql = "SELECT * FROM customer";
            break;
        }

        // Insert data to customer
        case 301: {
            $sql = "INSERT INTO customer(name,phone,email,age,address,district,city,zalo,facebook)
            		VALUES('$data->name','$data->phone','$data->email','$data->age','$data->address','$data->district','$data->city','$data->zalo','$data->facebook')";
            break;
        }

        // Update data customer
        case 302: {
            $sql = "UPDATE customer SET name='$data->name', phone='$data->phone', email='$data->email', age='$data->age', address='$data->address', district='$data->district', city='$data->city', zalo='$data->zalo', facebook = '$data->facebook'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of customer
        case 303: {
            $sql = "DELETE FROM customer
            		WHERE id IN($data->id)";
            break;
        }

        // Find data with id customer
        case 304: {
            $sql = "SELECT * FROM customer
            		WHERE id='$data->id'";
            break;
        }

        // Select with pagination(offset, number-item-in-page) customer
        case 305: {
            $sql = "SELECT * FROM customer
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of customer
        case 306: {
            $sql = "SELECT COUNT(1) FROM customer ";
            break;
        }

	}
?> 
