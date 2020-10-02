<?php 
	switch ($data->what) { 
        //******************sell************************
        // sell(id,idproduct,idcustomer,idstaff,status,amount,price,createdate,pay,note,customerstatus,datecall,customernote,statusliabilities,datepay,noteliabilities)
        // Get all data from sell
        case 400: {
            $sql = "SELECT * FROM sell";
            break;
        }

        // Insert data to sell
        case 401: {
            $sql = "INSERT INTO sell(idproduct,idcustomer,idstaff,status,amount,price,createdate,pay,note,customerstatus,datecall,customernote,statusliabilities,datepay,noteliabilities)
            		VALUES('$data->idproduct','$data->idcustomer','$data->idstaff','$data->status','$data->amount','$data->price','$data->createdate','$data->pay','$data->note','$data->customerstatus','$data->datecall','$data->customernote','$data->statusliabilities','$data->datepay','$data->noteliabilities')";
            break;
        }

        // Update data sell
        case 402: {
            $sql = "UPDATE sell SET idproduct='$data->idproduct', idcustomer='$data->idcustomer', idstaff='$data->idstaff', status='$data->status', amount='$data->amount', price='$data->price', createdate='$data->createdate', pay='$data->pay', note='$data->note', customerstatus='$data->customerstatus', datecall='$data->datecall', customernote='$data->customernote', statusliabilities='$data->statusliabilities', datepay='$data->datepay', noteliabilities = '$data->noteliabilities'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sell
        case 403: {
            $sql = "DELETE FROM sell
            		WHERE id IN($data->id)";
            break;
        }

        // Find data with id sell
        case 404: {
            $sql = "SELECT * FROM sell
            		WHERE id='$data->id'";
            break;
        }

        // Select with pagination(offset, number-item-in-page) sell
        case 405: {
            $sql = "SELECT * FROM sell
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Count number item of sell
        case 406: {
            $sql = "SELECT COUNT(1) FROM sell ";
            break;
        }

	}
?> 
