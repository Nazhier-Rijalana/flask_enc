<?php 
function rot3($str){
	$d = array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	$a = array("d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C");
	$i=0;
	foreach($d as $dd){
		if($dd==$str){
			break;
		}
		$i++;
	}
	return $a[$i];
}

function d_rot3($str){
	$a = array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	$d = array("d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C");
	$i=0;
	foreach($d as $dd){
		if($dd==$str){
			break;
		}
		$i++;
	}
	return $a[$i];
}


function get_index($str){
	$d = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	$i=0;
	foreach($d as $dd){
		if($dd==$str){
		return $i;
			break;
		}
		$i++;
	}
}

function get_str($i){
	$d = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	return $d[$i];
}

function balik($index){
	$d = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	return $d[$index];
}




function geser($plain){
	$kt = strtoupper($plain);
	$kt = str_replace(" ","",$kt);

	$kunci = 11;

	$data = str_split($kt);

	$i=0;
	foreach($data as $aaa)
	{
		$ee = get_index($aaa);
		$h= $ee+$kunci;
		if($h>=26){
			$ss[$i] = ($ee+11)-26;
		}
		else
		{
			$ss[$i] = $ee+$kunci;
		}
		$i++;
	}
	
	$i=0;
	foreach($ss as $ccc)
	{
		$gs[$i] = balik($ccc);
		$i++;
	}
	$geser = implode($gs);
	return $geser;
}



function d_geser($chiper){
	$kt = strtoupper($chiper);
		$kt = str_replace(" ","",$kt);

		$kunci = 11;

		$data = str_split($kt);
		
		$i=0;
		foreach($data as $aaa)
		{
			$ee = get_index($aaa);
			
			
			$dd = $ee + 26-11;
			if($dd>=26){
				$gg = $dd-26;
				//echo"$gg ";
				$ss[$i]=get_str($gg);
			}
			else
			{
				//echo"$dd ";
				$ss[$i]=get_str($dd);
			}
			$i++;
		}
		
		$ffg = implode($ss);
		return $ffg;
}

function get_navigasi($modul){
	$nav="<ul>";
	$nav.="<li ";if($modul==""){$nav.="class=\"aktiv\" ";}$nav.="><a href=\"./\" title=\"\">Home</a></li>";
	$nav.="<li ";if($modul=="rot3_geser"){$nav.="class=\"aktiv\" ";}$nav.="><a href=\"?m=rot3_geser\" title=\"\">Rot3 + Geser</a><ul><li><a href=\"#\">hello</a></li></ul></li>";
	$nav.="<li ";if($modul=="rot3"){$nav.="class=\"aktiv\" ";}$nav.="><a href=\"?m=rot3\" title=\"\">Rot3</a></li>";
	$nav.="<li ";if($modul=="geser"){$nav.="class=\"aktiv\" ";}$nav.="><a href=\"?m=geser\" title=\"\">Geser</a></li>";
	$nav.="<li ";if($modul=="about"){$nav.="class=\"aktiv\" ";}$nav.="><a href=\"?m=about\" title=\"\">About</a></li>";
		
	$nav .="</ul>";
	
	return $nav;
}
?>