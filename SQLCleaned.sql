with recursive numbers as
(select 1 as n
union all
select n+1 from numbers
where n<999
)

select 	id_index,
		header,
		content,
        lower(substring_index(substring_index(content," ",n)," ",-1)) as words,
		(char_length(content)-char_length(replace(content," ",""))+1) as Length,
		n as iterations
from mobytablemsdos m join numbers n
on n.n <= (char_length(content)-char_length(replace(content," ",""))+1)
where isActive = 1 and header like '%Chapter%'

# select * from results;