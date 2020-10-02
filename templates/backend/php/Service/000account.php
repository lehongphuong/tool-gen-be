<?php 
	switch ($data->what) { 
        //******************p000account************************
        // p000account(id,name,email,phone,address,role,created_date)
		// Get all data from 0 staff
        case 0: {
            $sql = "SELECT * FROM p000account";
            break;
        }

		// Insert data to p000account
        case 1: {
            $sql = "INSERT INTO p000account(name,email,phone,address,img,role)
            		VALUES('$data->name','$data->email','$data->phone','$data->address','$data->img','$data->role')";
            break;
        }

		// Update data p000account
        case 2: {
            $sql = "UPDATE p000account SET name='$data->name', email='$data->email', phone='$data->phone',address='$data->address', role='$data->role', created_date = '$data->created_date'
            		WHERE id='$data->id'";
            break;
        }

		// Delete data of p000account
        case 3: {
            $sql = "DELETE FROM p000account
            		WHERE id IN($data->listid)";
            break;
        }

        // check gmail candidate
        case 4: {
            $sql = "SELECT email FROM p000account
					WHERE email = '$data->email'";
            break;
        }

		// login candidate
        case 5: {
            $sql = "SELECT * FROM p000account
					WHERE email='$data->email' AND password='$data->password'";
            break;
        }

		// get staff with id
		case 6: {
            $sql = "SELECT * FROM p000account WHERE id='$data->id'";
            break;
        }

		 // change pass md5
        case 7: {
            $sql = "UPDATE p000account SET password='$data->password' WHERE id='$data->id'";
            break;
        }

		// update info staff
		case 8: {
            $sql = "UPDATE p000account SET name='$data->name' WHERE id='$data->id'";
            break;
        }

		// update info avatar
        case 9: {
            $sql = "UPDATE p000account SET img='$data->img' WHERE id='$data->id'";
            break;
        }

		// Select with pagination(offset, number-item-in-page) p000account
        case 10: {
            $sql = "SELECT * FROM p000account
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of p000account
        case 11: {
            $sql = "SELECT COUNT(1) FROM p000account ";
            break;
        }
	}
?> 
