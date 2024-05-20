/* create table results_grouped
select header, words, count(words) as word_count from results
group by header, words; */

select * from results_grouped;