<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header('Access-Control-Allow-Headers: Origin, Content-Type, Authorization, X-Auth-Token');
header('Access-Control-Allow-Methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS');
header('Content-Type: text/html; charset=utf-8');
include "db.php";
$data = json_decode(file_get_contents("php://input"));

//include "db.php";
$sql = "";
//$data = base64_decode("W29iamVjdCBPYmplY3Rd");
// echo json_encode($data);

// $param = file_get_contents("php://input");

// decode param data
for($i = 0; $i < 3; $i++){
    // $param = base64_decode($param); 
} 

// decode param data 

//$data = json_decode($param);
//$sql = $data;

if (isset($data->what)) { 

    switch ($data->what) {
        
        // excute string query
        case 0: {
            $sql = $data->sql;
            break;
        } 
		
		// 10 sys_menu(id,ptypeid,siteid,title,keyword,arrange,position,approved,lang,url,intranet)
		// 20 sys_configsite(id,siteid,title,keywords,description,footer,approved,lang)
		// 30 sys_functions(id,title,typeid,arrange,icon,link)
		// 40 sys_member(id,maphongban,manhom,kyvanban,name,siteid,password,username,postdate,approved,level,permission,email)
		// 50 sys_position(id,title,approved)
		// 60 sys_sites(id,name,keyword,url,approved)
		// 70 sys_templates(id,siteid,title,folder,imagepath,approved)
		// 80 sys_banner(id,siteid,title,link,arrange,approved,lang,pathimage)
		// 90 contents(id,typeid,siteid,title,url,summary,content,pathfile,pathimage,comment,postdate,changedate,approved,lang,author)
		// 100 news(id,typeid,siteid,title,url,postdate,changedate,summary,content,pathimage,author,approved,comment,lang,isfocus,isNew,view)
		// 110 documents(id,typeid,siteid,title,url,content,pathfile,postdate,changedate,approved,lang,author)
		// 120 album(id,siteid,title,arrange,approved,lang,pathimage,description,postdate)
		// 130 photos(id,typeid,title,pathimage,postdate,approved,lang,arrange)
		// 140 supportonline(id,siteid,typeid,nick,name,approved,arrange,note,phone)
		// 150 contactus(id,siteid,title,content,approved,lang,email)
		// 160 weblink(id,siteid,title,link,approved,arrange,lang)
		// 170 feedbacks(id,siteid,name,email,phone,address,title,content,approved,lang,postdate,reply)
		// 180 trungcauykien(id)
		// 190 advertises_type(id,keyword,title,approved)
		// 200 advertises(id,siteid,title,pathimage,position,approved,arrange,link,lang)
		// 210 schedule(id,sdate,stime,content,stakeholder,location,host,approved,postdate,lang)
		
        //******************sys_menu************************
        // sys_menu(id,ptypeid,siteid,title,keyword,arrange,position,approved,lang,url,intranet)
        // Get all data from sys_menu
        case 10: {
            $sql = "SELECT * FROM sys_menu";
            break;
        }

        // Insert data to sys_menu
        case 11: {
            $sql = "INSERT INTO sys_menu(ptypeid,siteid,title,keyword,arrange,position,approved,lang,url,intranet)
            		VALUES('$data->ptypeid','$data->siteid','$data->title','$data->keyword','$data->arrange','$data->position','$data->approved','$data->lang','$data->url','$data->intranet')";
            break;
        }

        // Update data sys_menu
        case 12: {
            $sql = "UPDATE sys_menu SET ptypeid='$data->ptypeid', siteid='$data->siteid', title='$data->title', keyword='$data->keyword', arrange='$data->arrange', position='$data->position', approved='$data->approved', lang='$data->lang', url='$data->url', intranet = '$data->intranet'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_menu
        case 13: {
            $sql = "DELETE FROM sys_menu
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_menu
        case 14: {
            $sql = "SELECT * FROM sys_menu
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_menu
        case 15: {
            $sql = "SELECT t1.*, t2.id as id1, t2.ptypeid as ptypeid1, t2.siteid as siteid1, t2.title as title1, t2.keyword as keyword1, t2.arrange as arrange1, t2.position as position1, t2.approved as approved1, t2.lang as lang1, t2.url as url1, t2.intranet as intranet1
					FROM sys_menu t1 
						LEFT JOIN sys_menu t2 ON t1.id = t2.ptypeid 
					WHERE t1.ptypeid = 0
					ORDER BY t1.id, t1.arrange";
            break;
        }

        // Find data with id sys_menu
        case 16: {
            $sql = "SELECT COUNT(1) FROM sys_menu ";
            break;
        }
		
		case 17: {
            $sql = "SELECT t1.*, t2.id as id1, t2.ptypeid as ptypeid1, t2.siteid as siteid1, t2.title as title1, t2.keyword as keyword1, t2.arrange as arrange1, t2.position as position1, t2.approved as approved1, t2.lang as lang1, t2.url as url1, t2.intranet as intranet1
					FROM sys_menu t1 
						LEFT JOIN sys_menu t2 ON t1.id = t2.ptypeid 
					WHERE t1.ptypeid = 0  
						AND t1.lang ='$data->lang' 
						AND t1.siteid = '$data->siteid'
					ORDER BY t1.id, t1.arrange";
            break;
        }


        //******************sys_configsite************************
        // sys_configsite(id,siteid,title,keywords,description,footer,approved,lang)
        // Get all data from sys_configsite
        case 20: {
            $sql = "SELECT * FROM sys_configsite";
            break;
        }

        // Insert data to sys_configsite
        case 21: {
            $sql = "INSERT INTO sys_configsite(siteid,title,keywords,description,footer,approved,lang)
            		VALUES('$data->siteid','$data->title','$data->keywords','$data->description','$data->footer','$data->approved','$data->lang')";
            break;
        }

        // Update data sys_configsite
        case 22: {
            $sql = "UPDATE sys_configsite SET siteid='$data->siteid', title='$data->title', keywords='$data->keywords', description='$data->description', footer='$data->footer', approved='$data->approved', lang = '$data->lang'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_configsite
        case 23: {
            $sql = "DELETE FROM sys_configsite
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_configsite
        case 24: {
            $sql = "SELECT * FROM sys_configsite
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_configsite
        case 25: {
			if($data->approved=='2' && $data->siteid=='0'){
				$sql = "SELECT * FROM sys_configsite
						WHERE lang = '$data->lang'";
			}else{
				if($data->approved=='2'){
					$sql = "SELECT * FROM sys_configsite
							WHERE siteid = '$data->siteid' 
								AND lang = '$data->lang'";
				}else{
					if($data->siteid=='0'){
						$sql = "SELECT * FROM sys_configsite
								WHERE approved = '$data->approved' 
									AND lang = '$data->lang'";
					}else{
						$sql = "SELECT * FROM sys_configsite
							WHERE siteid = '$data->siteid' 
								AND approved = '$data->approved'
								AND lang = '$data->lang'";
					}
				}  
			}
		  
            
            break;
        }

        // Update approved status to one
        case 26: {
            $sql = "UPDATE sys_configsite SET approved='1'
            		WHERE id IN($data->listid)";
            break;
        }
		
		// Delete many item 
        case 27: {
            $sql = "DELETE FROM sys_configsite
            		WHERE id IN($data->listid)";
            break;
        }



        //******************sys_functions************************
        // sys_functions(id,title,typeid,arrange,icon,link)
        // Get all data from sys_functions
        case 30: {
            $sql = "SELECT * FROM sys_functions";
            break;
        }

        // Insert data to sys_functions
        case 31: {
            $sql = "INSERT INTO sys_functions(title,typeid,arrange,icon,link)
            		VALUES('$data->title','$data->typeid','$data->arrange','$data->icon','$data->link')";
            break;
        }

        // Update data sys_functions
        case 32: {
            $sql = "UPDATE sys_functions SET title='$data->title', typeid='$data->typeid', arrange='$data->arrange', icon='$data->icon', link = '$data->link'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_functions
        case 33: {
            $sql = "DELETE FROM sys_functions
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_functions
        case 34: {
            $sql = "SELECT * FROM sys_functions
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_functions
        case 35: {
            $sql = "SELECT * FROM sys_functions
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_functions
        case 36: {
            $sql = "SELECT COUNT(1) FROM sys_functions ";
            break;
        }


        //******************sys_member************************
        // sys_member(id,maphongban,manhom,kyvanban,name,siteid,password,username,postdate,approved,level,permission,email)
        // Get all data from sys_member
        case 40: {
            $sql = "SELECT * FROM sys_member";
            break;
        }

        // Insert data to sys_member
        case 41: {
            $sql = "INSERT INTO sys_member(maphongban,manhom,kyvanban,name,siteid,password,username,postdate,approved,level,permission,email)
            		VALUES('$data->maphongban','$data->manhom','$data->kyvanban','$data->name','$data->siteid','$data->password','$data->username','$data->postdate','$data->approved','$data->level','$data->permission','$data->email')";
            break;
        }

        // Update data sys_member
        case 42: {
            $sql = "UPDATE sys_member SET maphongban='$data->maphongban', manhom='$data->manhom', kyvanban='$data->kyvanban', name='$data->name', siteid='$data->siteid', password='$data->password', username='$data->username', postdate='$data->postdate', approved='$data->approved', level='$data->level', permission='$data->permission', email = '$data->email'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_member
        case 43: {
            $sql = "DELETE FROM sys_member
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_member
        case 44: {
            $sql = "SELECT * FROM sys_member
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_member
        case 45: {
            $sql = "SELECT * FROM sys_member
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_member
        case 46: {
            $sql = "SELECT COUNT(1) FROM sys_member ";
            break;
        }


        //******************sys_position************************
        // sys_position(id,title,approved)
        // Get all data from sys_position
        case 50: {
            $sql = "SELECT * FROM sys_position";
            break;
        }

        // Insert data to sys_position
        case 51: {
            $sql = "INSERT INTO sys_position(title,approved)
            		VALUES('$data->title','$data->approved')";
            break;
        }

        // Update data sys_position
        case 52: {
            $sql = "UPDATE sys_position SET title='$data->title', approved = '$data->approved'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_position
        case 53: {
            $sql = "DELETE FROM sys_position
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_position
        case 54: {
            $sql = "SELECT * FROM sys_position
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_position
        case 55: {
            $sql = "SELECT * FROM sys_position
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_position
        case 56: {
            $sql = "SELECT COUNT(1) FROM sys_position ";
            break;
        }


        //******************sys_sites************************
        // sys_sites(id,name,keyword,url,approved)
        // Get all data from sys_sites
        case 60: {
            $sql = "SELECT * FROM sys_sites";
            break;
        }

        // Insert data to sys_sites
        case 61: {
            $sql = "INSERT INTO sys_sites(name,keyword,url,approved)
            		VALUES('$data->name','$data->keyword','$data->url','$data->approved')";
            break;
        }

        // Update data sys_sites
        case 62: {
            $sql = "UPDATE sys_sites SET name='$data->name', keyword='$data->keyword', url='$data->url', approved = '$data->approved'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_sites
        case 63: {
            $sql = "DELETE FROM sys_sites
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_sites
        case 64: {
            $sql = "SELECT * FROM sys_sites
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_sites
        case 65: {
            $sql = "SELECT * FROM sys_sites
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_sites
        case 66: {
            $sql = "SELECT COUNT(1) FROM sys_sites ";
            break;
        }


        //******************sys_templates************************
        // sys_templates(id,siteid,title,folder,imagepath,approved)
        // Get all data from sys_templates
        case 70: {
            $sql = "SELECT * FROM sys_templates";
            break;
        }

        // Insert data to sys_templates
        case 71: {
            $sql = "INSERT INTO sys_templates(siteid,title,folder,imagepath,approved)
            		VALUES('$data->siteid','$data->title','$data->folder','$data->imagepath','$data->approved')";
            break;
        }

        // Update data sys_templates
        case 72: {
            $sql = "UPDATE sys_templates SET siteid='$data->siteid', title='$data->title', folder='$data->folder', imagepath='$data->imagepath', approved = '$data->approved'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_templates
        case 73: {
            $sql = "DELETE FROM sys_templates
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_templates
        case 74: {
            $sql = "SELECT * FROM sys_templates
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_templates
        case 75: {
            $sql = "SELECT * FROM sys_templates
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_templates
        case 76: {
            $sql = "SELECT COUNT(1) FROM sys_templates ";
            break;
        }


        //******************sys_banner************************
        // sys_banner(id,siteid,title,link,arrange,approved,lang,pathimage)
        // Get all data from sys_banner
        case 80: {
            $sql = "SELECT * FROM sys_banner";
            break;
        }

        // Insert data to sys_banner
        case 81: {
            $sql = "INSERT INTO sys_banner(siteid,title,link,arrange,approved,lang,pathimage)
            		VALUES('$data->siteid','$data->title','$data->link','$data->arrange','$data->approved','$data->lang','$data->pathimage')";
            break;
        }

        // Update data sys_banner
        case 82: {
            $sql = "UPDATE sys_banner SET siteid='$data->siteid', title='$data->title', link='$data->link', arrange='$data->arrange', approved='$data->approved', lang='$data->lang', pathimage = '$data->pathimage'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of sys_banner
        case 83: {
            $sql = "DELETE FROM sys_banner
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_banner
        case 84: {
            $sql = "SELECT * FROM sys_banner
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id sys_banner
        case 85: {
            $sql = "SELECT * FROM sys_banner
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id sys_banner
        case 86: {
            $sql = "SELECT COUNT(1) FROM sys_banner ";
            break;
        }


        //******************contents************************
        // contents(id,typeid,siteid,title,url,summary,content,pathfile,pathimage,comment,postdate,changedate,approved,lang,author)
        // Get all data from contents
        case 90: {
            $sql = "SELECT * FROM contents";
            break;
        }

        // Insert data to contents
        case 91: {
            $sql = "INSERT INTO contents(typeid,siteid,title,url,summary,content,pathfile,pathimage,comment,postdate,changedate,approved,lang,author)
            		VALUES('$data->typeid','$data->siteid','$data->title','$data->url','$data->summary','$data->content','$data->pathfile','$data->pathimage','$data->comment','$data->postdate','$data->changedate','$data->approved','$data->lang','$data->author')";
            break;
        }

        // Update data contents
        case 92: {
            $sql = "UPDATE contents SET typeid='$data->typeid', siteid='$data->siteid', title='$data->title', url='$data->url', summary='$data->summary', content='$data->content', pathfile='$data->pathfile', pathimage='$data->pathimage', comment='$data->comment', postdate='$data->postdate', changedate='$data->changedate', approved='$data->approved', lang='$data->lang', author = '$data->author'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of contents
        case 93: {
            $sql = "DELETE FROM contents
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id contents
        case 94: {
            $sql = "SELECT * FROM contents
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id contents
        case 95: {
            $sql = "SELECT * FROM contents
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id contents
        case 96: {
            $sql = "SELECT COUNT(1) FROM contents ";
            break;
        }


        //******************news************************
        // news(id,typeid,siteid,title,url,postdate,changedate,summary,content,pathimage,author,approved,comment,lang,isfocus,isNew,view)
        // Get all data from news
        case 100: {
            $sql = "SELECT * FROM news";
            break;
        }

        // Insert data to news
        case 101: {
            $sql = "INSERT INTO news(typeid,siteid,title,url,postdate,changedate,summary,content,pathimage,author,approved,comment,lang,isfocus,isNew,view)
            		VALUES('$data->typeid','$data->siteid','$data->title','$data->url','$data->postdate','$data->changedate','$data->summary','$data->content','$data->pathimage','$data->author','$data->approved','$data->comment','$data->lang','$data->isfocus','$data->isNew','$data->view')";
            break;
        }

        // Update data news
        case 102: {
            $sql = "UPDATE news SET typeid='$data->typeid', siteid='$data->siteid', title='$data->title', url='$data->url', postdate='$data->postdate', changedate='$data->changedate', summary='$data->summary', content='$data->content', pathimage='$data->pathimage', author='$data->author', approved='$data->approved', comment='$data->comment', lang='$data->lang', isfocus='$data->isfocus', isNew='$data->isNew', view = '$data->view'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of news
        case 103: {
            $sql = "DELETE FROM news
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id news
        case 104: {
            $sql = "SELECT * FROM news
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id news
        case 105: {
            $sql = "SELECT * FROM news
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id news
        case 106: {
            $sql = "SELECT COUNT(1) FROM news ";
            break;
        }


        //******************documents************************
        // documents(id,typeid,siteid,title,url,content,pathfile,postdate,changedate,approved,lang,author)
        // Get all data from documents
        case 110: {
            $sql = "SELECT * FROM documents";
            break;
        }

        // Insert data to documents
        case 111: {
            $sql = "INSERT INTO documents(typeid,siteid,title,url,content,pathfile,postdate,changedate,approved,lang,author)
            		VALUES('$data->typeid','$data->siteid','$data->title','$data->url','$data->content','$data->pathfile','$data->postdate','$data->changedate','$data->approved','$data->lang','$data->author')";
            break;
        }

        // Update data documents
        case 112: {
            $sql = "UPDATE documents SET typeid='$data->typeid', siteid='$data->siteid', title='$data->title', url='$data->url', content='$data->content', pathfile='$data->pathfile', postdate='$data->postdate', changedate='$data->changedate', approved='$data->approved', lang='$data->lang', author = '$data->author'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of documents
        case 113: {
            $sql = "DELETE FROM documents
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id documents
        case 114: {
            $sql = "SELECT * FROM documents
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id documents
        case 115: {
            $sql = "SELECT * FROM documents
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id documents
        case 116: {
            $sql = "SELECT COUNT(1) FROM documents ";
            break;
        }


        //******************album************************
        // album(id,siteid,title,arrange,approved,lang,pathimage,description,postdate)
        // Get all data from album
        case 120: {
            $sql = "SELECT * FROM album";
            break;
        }

        // Insert data to album
        case 121: {
            $sql = "INSERT INTO album(siteid,title,arrange,approved,lang,pathimage,description,postdate)
            		VALUES('$data->siteid','$data->title','$data->arrange','$data->approved','$data->lang','$data->pathimage','$data->description','$data->postdate')";
            break;
        }

        // Update data album
        case 122: {
            $sql = "UPDATE album SET siteid='$data->siteid', title='$data->title', arrange='$data->arrange', approved='$data->approved', lang='$data->lang', pathimage='$data->pathimage', description='$data->description', postdate = '$data->postdate'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of album
        case 123: {
            $sql = "DELETE FROM album
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id album
        case 124: {
            $sql = "SELECT * FROM album
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id album
        case 125: {
            $sql = "SELECT * FROM album
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id album
        case 126: {
            $sql = "SELECT COUNT(1) FROM album ";
            break;
        }


        //******************photos************************
        // photos(id,typeid,title,pathimage,postdate,approved,lang,arrange)
        // Get all data from photos
        case 130: {
            $sql = "SELECT * FROM photos";
            break;
        }

        // Insert data to photos
        case 131: {
            $sql = "INSERT INTO photos(typeid,title,pathimage,postdate,approved,lang,arrange)
            		VALUES('$data->typeid','$data->title','$data->pathimage','$data->postdate','$data->approved','$data->lang','$data->arrange')";
            break;
        }

        // Update data photos
        case 132: {
            $sql = "UPDATE photos SET typeid='$data->typeid', title='$data->title', pathimage='$data->pathimage', postdate='$data->postdate', approved='$data->approved', lang='$data->lang', arrange = '$data->arrange'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of photos
        case 133: {
            $sql = "DELETE FROM photos
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id photos
        case 134: {
            $sql = "SELECT * FROM photos
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id photos
        case 135: {
            $sql = "SELECT * FROM photos
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id photos
        case 136: {
            $sql = "SELECT COUNT(1) FROM photos ";
            break;
        }


        //******************supportonline************************
        // supportonline(id,siteid,typeid,nick,name,approved,arrange,note,phone)
        // Get all data from supportonline
        case 140: {
            $sql = "SELECT * FROM supportonline";
            break;
        }

        // Insert data to supportonline
        case 141: {
            $sql = "INSERT INTO supportonline(siteid,typeid,nick,name,approved,arrange,note,phone)
            		VALUES('$data->siteid','$data->typeid','$data->nick','$data->name','$data->approved','$data->arrange','$data->note','$data->phone')";
            break;
        }

        // Update data supportonline
        case 142: {
            $sql = "UPDATE supportonline SET siteid='$data->siteid', typeid='$data->typeid', nick='$data->nick', name='$data->name', approved='$data->approved', arrange='$data->arrange', note='$data->note', phone = '$data->phone'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of supportonline
        case 143: {
            $sql = "DELETE FROM supportonline
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id supportonline
        case 144: {
            $sql = "SELECT * FROM supportonline
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id supportonline
        case 145: {
            $sql = "SELECT * FROM supportonline
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id supportonline
        case 146: {
            $sql = "SELECT COUNT(1) FROM supportonline ";
            break;
        }


        //******************contactus************************
        // contactus(id,siteid,title,content,approved,lang,email)
        // Get all data from contactus
        case 150: {
            $sql = "SELECT * FROM contactus";
            break;
        }

        // Insert data to contactus
        case 151: {
            $sql = "INSERT INTO contactus(siteid,title,content,approved,lang,email)
            		VALUES('$data->siteid','$data->title','$data->content','$data->approved','$data->lang','$data->email')";
            break;
        }

        // Update data contactus
        case 152: {
            $sql = "UPDATE contactus SET siteid='$data->siteid', title='$data->title', content='$data->content', approved='$data->approved', lang='$data->lang', email = '$data->email'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of contactus
        case 153: {
            $sql = "DELETE FROM contactus
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id contactus
        case 154: {
            $sql = "SELECT * FROM contactus
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id contactus
        case 155: {
            $sql = "SELECT * FROM contactus
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id contactus
        case 156: {
            $sql = "SELECT COUNT(1) FROM contactus ";
            break;
        }


        //******************weblink************************
        // weblink(id,siteid,title,link,approved,arrange,lang)
        // Get all data from weblink
        case 160: {
            $sql = "SELECT * FROM weblink";
            break;
        }

        // Insert data to weblink
        case 161: {
            $sql = "INSERT INTO weblink(siteid,title,link,approved,arrange,lang)
            		VALUES('$data->siteid','$data->title','$data->link','$data->approved','$data->arrange','$data->lang')";
            break;
        }

        // Update data weblink
        case 162: {
            $sql = "UPDATE weblink SET siteid='$data->siteid', title='$data->title', link='$data->link', approved='$data->approved', arrange='$data->arrange', lang = '$data->lang'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of weblink
        case 163: {
            $sql = "DELETE FROM weblink
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id weblink
        case 164: {
            $sql = "SELECT * FROM weblink
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id weblink
        case 165: {
            $sql = "SELECT * FROM weblink
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id weblink
        case 166: {
            $sql = "SELECT COUNT(1) FROM weblink ";
            break;
        }


        //******************feedbacks************************
        // feedbacks(id,siteid,name,email,phone,address,title,content,approved,lang,postdate,reply)
        // Get all data from feedbacks
        case 170: {
            $sql = "SELECT * FROM feedbacks";
            break;
        }

        // Insert data to feedbacks
        case 171: {
            $sql = "INSERT INTO feedbacks(siteid,name,email,phone,address,title,content,approved,lang,postdate,reply)
            		VALUES('$data->siteid','$data->name','$data->email','$data->phone','$data->address','$data->title','$data->content','$data->approved','$data->lang','$data->postdate','$data->reply')";
            break;
        }

        // Update data feedbacks
        case 172: {
            $sql = "UPDATE feedbacks SET siteid='$data->siteid', name='$data->name', email='$data->email', phone='$data->phone', address='$data->address', title='$data->title', content='$data->content', approved='$data->approved', lang='$data->lang', postdate='$data->postdate', reply = '$data->reply'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of feedbacks
        case 173: {
            $sql = "DELETE FROM feedbacks
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id feedbacks
        case 174: {
            $sql = "SELECT * FROM feedbacks
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id feedbacks
        case 175: {
            $sql = "SELECT * FROM feedbacks
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id feedbacks
        case 176: {
            $sql = "SELECT COUNT(1) FROM feedbacks ";
            break;
        }


        //******************trungcauykien************************
        // trungcauykien(id)
        // Get all data from trungcauykien
        case 180: {
            $sql = "SELECT * FROM trungcauykien";
            break;
        }

        // Insert data to trungcauykien
        case 181: {
            $sql = "INSERT INTO trungcauykien(trungcauykien(id)
            		VALUES('$data->id')";
            break;
        }

        // Update data trungcauykien
        case 182: {
            $sql = "UPDATE trungcauykien SET id = '$data->id'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of trungcauykien
        case 183: {
            $sql = "DELETE FROM trungcauykien
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id trungcauykien
        case 184: {
            $sql = "SELECT * FROM trungcauykien
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id trungcauykien
        case 185: {
            $sql = "SELECT * FROM trungcauykien
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id trungcauykien
        case 186: {
            $sql = "SELECT COUNT(1) FROM trungcauykien ";
            break;
        }


        //******************advertises_type************************
        // advertises_type(id,keyword,title,approved)
        // Get all data from advertises_type
        case 190: {
            $sql = "SELECT * FROM advertises_type";
            break;
        }

        // Insert data to advertises_type
        case 191: {
            $sql = "INSERT INTO advertises_type(keyword,title,approved)
            		VALUES('$data->keyword','$data->title','$data->approved')";
            break;
        }

        // Update data advertises_type
        case 192: {
            $sql = "UPDATE advertises_type SET keyword='$data->keyword', title='$data->title', approved = '$data->approved'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of advertises_type
        case 193: {
            $sql = "DELETE FROM advertises_type
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id advertises_type
        case 194: {
            $sql = "SELECT * FROM advertises_type
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id advertises_type
        case 195: {
            $sql = "SELECT * FROM advertises_type
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id advertises_type
        case 196: {
            $sql = "SELECT COUNT(1) FROM advertises_type ";
            break;
        }


        //******************advertises************************
        // advertises(id,siteid,title,pathimage,position,approved,arrange,link,lang)
        // Get all data from advertises
        case 200: {
            $sql = "SELECT * FROM advertises";
            break;
        }

        // Insert data to advertises
        case 201: {
            $sql = "INSERT INTO advertises(siteid,title,pathimage,position,approved,arrange,link,lang)
            		VALUES('$data->siteid','$data->title','$data->pathimage','$data->position','$data->approved','$data->arrange','$data->link','$data->lang')";
            break;
        }

        // Update data advertises
        case 202: {
            $sql = "UPDATE advertises SET siteid='$data->siteid', title='$data->title', pathimage='$data->pathimage', position='$data->position', approved='$data->approved', arrange='$data->arrange', link='$data->link', lang = '$data->lang'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of advertises
        case 203: {
            $sql = "DELETE FROM advertises
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id advertises
        case 204: {
            $sql = "SELECT * FROM advertises
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id advertises
        case 205: {
            $sql = "SELECT * FROM advertises
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id advertises
        case 206: {
            $sql = "SELECT COUNT(1) FROM advertises ";
            break;
        }


        //******************schedule************************
        // schedule(id,sdate,stime,content,stakeholder,location,host,approved,postdate,lang)
        // Get all data from schedule
        case 210: {
            $sql = "SELECT * FROM schedule";
            break;
        }

        // Insert data to schedule
        case 211: {
            $sql = "INSERT INTO schedule(sdate,stime,content,stakeholder,location,host,approved,postdate,lang)
            		VALUES('$data->sdate','$data->stime','$data->content','$data->stakeholder','$data->location','$data->host','$data->approved','$data->postdate','$data->lang')";
            break;
        }

        // Update data schedule
        case 212: {
            $sql = "UPDATE schedule SET sdate='$data->sdate', stime='$data->stime', content='$data->content', stakeholder='$data->stakeholder', location='$data->location', host='$data->host', approved='$data->approved', postdate='$data->postdate', lang = '$data->lang'
            		WHERE id='$data->id'";
            break;
        }

        // Delete data of schedule
        case 213: {
            $sql = "DELETE FROM schedule
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id schedule
        case 214: {
            $sql = "SELECT * FROM schedule
            		WHERE id='$data->id'";
            break;
        }

        // Find data with id schedule
        case 215: {
            $sql = "SELECT * FROM schedule
            		LIMIT $data->offset, $data->limit";
            break;
        }

        // Find data with id schedule
        case 216: {
            $sql = "SELECT COUNT(1) FROM schedule ";
            break;
        }  
        
    }
    
    // echo $sql."<br>";
    
    //excute sql 
    $result = $conn->query($sql);
    
    // echo json_encode($result);
    if (isset($result->num_rows) && ($result->num_rows > 0)) {
        // output data of each row 
        $data = array();
        while ($row = $result->fetch_assoc()) {
            $data[] = $row;
        }

        echo json_encode($data);
    } else {
        // echo json_encode($result);
        echo "{}";
    }
}
$conn->close();
?>