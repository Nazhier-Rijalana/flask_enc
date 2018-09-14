<?php
error_reporting(0);
$menu = $_GET[m];
include"lib.php";
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<title>ROT3</title>
	<link href="css/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
<div id="tabmenu">
	<ul id='subtabmenu'>
		<li <?php if($menu==""){echo" class=\"aktiv\" ";}?>><a href="./" title='Home'>Home</a></li>
		<li <?php if($menu=="rot3" or $menu=="geser" or $menu=="rot3_geser"){echo" class=\"aktiv\" ";}?>><a href='#'>Enkripsi</a>
			<ul>
				<li><a href="?m=rot3">ROT3</a></li>
				<li><a href="?m=geser">KODE GESER</a></li>
				<li><a href="?m=rot3_geser">ROT3 &amp; KODE GESER </a></li>
			</ul>
		</li>

		<li <?php if($menu=="d_rot3" or $menu=="d_geser" or $menu=="d_rot3_geser"){echo" class=\"aktiv\" ";}?>><a href='#'>Dekripsi</a>
			<ul>
				<li><a href="?m=d_rot3">ROT3</a></li>
				<li><a href="?m=d_geser">KODE GESER</a></li>
				<li><a href="?m=d_rot3_geser">ROT3 &amp; KODE GESER </a></li>
			</ul>
		</li>


		<li <?php if($menu=="about"){echo" class=\"aktiv\" ";}?>><a href="?m=about">About</a></li>
	</ul>
</div>





	<div id="body">


	</div>
</body>
</html>
