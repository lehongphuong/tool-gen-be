<?php 
	switch ($data->what) { 
        //******************staff************************
        // staff(id,fullname,username,password,phone,email,position,permission)
        // Get all data from staff
        case 10: {
            $sql = "SELECT * FROM staff";
            break;
        }

        // Insert data to staff
        case 11: {
            $sql = "INSERT INTO staff(fullname,username,password,phone,email,position,permission)
            		VALUES('$data->fullname','$data->username','$data->password','$data->phone','$data->email','$data->position','$data->permission')";
            break;
        }

        // Update data staff
        case 12: {
            $sql = "UPDATE staff SET fullname='$data->fullname', username='$data->username', password='$data->password', phone='$data->phone', email='$data->email', position='$data->position', permission = '$data->permission'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of staff
        case 13: {
            $sql = "DELETE FROM staff
            		WHERE id IN($data->id)";
            break;
        }

        // Find data with id staff
        case 14: {
            $sql = "SELECT * FROM staff
            		WHERE id='$data->id'";
            break;
        }

        // Select with pagination(offset, number-item-in-page) staff
        case 15: {
            $sql = "SELECT * FROM staff
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of staff
        case 16: {
            $sql = "SELECT COUNT(1) FROM staff ";
            break;
        }

	}
?> 
