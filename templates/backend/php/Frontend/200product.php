<?php 
	switch ($data->what) { 
        //******************product************************
        // product(id,name,price,cost,picture,origin)
        // Get all data from product
        case 200: {
            $sql = "SELECT * FROM product";
            break;
        }

        // Insert data to product
        case 201: {
            $sql = "INSERT INTO product(name,price,cost,picture,origin)
            		VALUES('$data->name','$data->price','$data->cost','$data->picture','$data->origin')";
            break;
        }

        // Update data product
        case 202: {
            $sql = "UPDATE product SET name='$data->name', price='$data->price', cost='$data->cost', picture='$data->picture', origin = '$data->origin'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of product
        case 203: {
            $sql = "DELETE FROM product
            		WHERE id IN($data->id)";
            break;
        }

        // Find data with id product
        case 204: {
            $sql = "SELECT * FROM product
            		WHERE id='$data->id'";
            break;
        }

        // Select with pagination(offset, number-item-in-page) product
        case 205: {
            $sql = "SELECT * FROM product
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of product
        case 206: {
            $sql = "SELECT COUNT(1) FROM product ";
            break;
        }

	}
?> 
