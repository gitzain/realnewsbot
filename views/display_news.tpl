<h1>News</h1>
<table>
<tr><th>Title</th><th>Link</th><th>Source</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>