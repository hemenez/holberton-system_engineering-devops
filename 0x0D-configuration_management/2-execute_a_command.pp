# Manifest will kill a process
exec { 'pkill killmenow':
  command => 'pkill killmenow'
}
