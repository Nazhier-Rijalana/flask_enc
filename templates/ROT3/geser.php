<h2>KODE GESER</h2>
<form action="" method="post" >
<table class="form">
	<tr><td>Plaintext<br /><textarea rows="3" cols="50" name="plain" ></textarea></td></tr>
	
	<tr><td><input type="submit" value="GO"/></td></tr>
</table>

</form>
	<?php 
if ($_SERVER['REQUEST_METHOD'] == 'POST')
{
	if(!empty($_POST[plain]))
	{
		$geser = geser($_POST[plain]);
	
		echo"

		<h3>Plaintext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$_POST[plain]</textarea></p>
		
		<h3>Chipertext</h3>
		<p><textarea rows=\"3\" cols=\"50\" >$geser</textarea></p>";
	}
	else
	{
		echo"<span style=\"color:#f00;\">Masukkan Plaintext...</span>";
	}
}
?>