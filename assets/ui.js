function v(id){const e=document.getElementById(id);return e?parseFloat(e.value)||0:0}
function rows(o){return '<table>'+o.map(([k,x])=>`<tr><td>${k}</td><td>${x}</td></tr>`).join('')+'</table>'}
function addRow(){document.querySelector('#items tbody').insertAdjacentHTML('beforeend','<tr><td><input></td><td><input type="number" value="1"></td><td><input type="number" value="0"></td></tr>')}
function runTool(){const t=document.querySelector('.tool');if(!t)return;const k=t.dataset.tool,out=document.getElementById('out');let h='';
if(k==='gig'){const r=gigProfit({pay:v('pay'),tips:v('tips'),fees:v('fees'),miles:v('miles'),mpg:v('mpg'),gas:v('gas'),wear:v('wear'),other:v('other'),hours:v('hours')});
 h=`<div class="big" id="result">${fmt(r.perHour)}/hr</div>`+rows([['Fuel cost',fmt(r.fuel)],['Wear & tear',fmt(r.wearCost)],['Net profit',fmt(r.net)],['Per mile',fmt(r.perMile)]]);}
if(k==='mile'){const r=mileageDeduction({miles:v('miles'),rate:v('rate'),tolls:v('tolls'),taxRate:v('taxRate')});h=`<div class="big" id="result">${fmt(r.deduction)}</div>`+rows([['Deduction',fmt(r.deduction)],['Approx. tax saved',fmt(r.estSavings)]]);}
if(k==='se'){const r=seTax({profit:v('profit'),w2:v('w2'),incomePct:v('incomePct')});h=`<div class="big" id="result">${fmt(r.quarterly)}/quarter</div>`+rows([['Social Security (12.4%)',fmt(r.ss)],['Medicare (2.9%)',fmt(r.medicare)],['Self-employment tax',fmt(r.se)],['Deductible half of SE tax',fmt(r.halfDeduct)],['Est. income tax',fmt(r.income)],['Total set-aside',fmt(r.total)]]);}
if(k==='rate'){const r=freelanceRate({income:v('income'),expenses:v('expenses'),hoursWeek:v('hoursWeek'),weeks:v('weeks'),taxPct:v('taxPct')});h=`<div class="big" id="result">${fmt(r.hourly)}/hr</div>`+rows([['Gross revenue needed',fmt(r.gross)],['Billable hours/yr',r.hours],['Day rate (8h)',fmt(r.day)]]);}
if(k==='goal'){const r=earningsGoal({goal:v('goal'),perHour:v('perHour'),daysWeek:v('daysWeek')});h=`<div class="big" id="result">${r.hours.toFixed(1)} hours</div>`+rows([['Hours per working day',r.perDay.toFixed(1)]]);}
if(k==='invoice'){const items=[...document.querySelectorAll('#items tbody tr')].map(tr=>{const i=tr.querySelectorAll('input');return{d:i[0].value,qty:i[1].value,rate:i[2].value}});
 const r=invoiceTotal(items,v('taxPct'),v('discount'));h=`<h3>Invoice #${document.getElementById('num').value}</h3><p>From: ${document.getElementById('from').value}<br>To: ${document.getElementById('to').value}</p>`+rows([['Subtotal',fmt(r.sub)],['Discount','-'+fmt(v('discount'))],['Tax',fmt(r.tax)]])+`<div class="big" id="result">${fmt(r.total)}</div>`;}
out.innerHTML=h}
document.addEventListener('DOMContentLoaded',runTool);
