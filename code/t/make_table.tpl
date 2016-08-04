%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p><h3>Your TODO Items:</h3></p>
<table border="1">
%for row in rows:
  %id, title = row
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="/edit/{{id}}"> Edit</a></td>
  </tr>
%end
</table>
<p>Create <a href="/new">New</a> item</p>
<p>Show <a href="/done">Done Items</a></p>