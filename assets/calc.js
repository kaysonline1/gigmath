/* GigMath pure calculation functions (also exported for Node tests) */
const SS_WAGE_BASE_2026 = 184500; // verify yearly at ssa.gov
const IRS_MILE_RATE_2026 = 0.725;  // verify yearly at irs.gov (standard mileage rates)
function gigProfit({pay=0,tips=0,fees=0,miles=0,mpg=25,gas=3.5,wear=0.10,other=0,hours=1}){
  const fuel = mpg>0 ? miles/mpg*gas : 0, wearCost = miles*wear;
  const net = pay+tips-fees-fuel-wearCost-other;
  return {fuel, wearCost, net, perHour: hours>0?net/hours:0, perMile: miles>0?net/miles:0};
}
function mileageDeduction({miles=0, rate=IRS_MILE_RATE_2026, tolls=0, taxRate=0.25}){
  const deduction = miles*rate + tolls;
  return {deduction, estSavings: deduction*taxRate};
}
function seTax({profit=0, w2=0, incomePct=12}){
  const base = Math.max(0, profit)*0.9235;
  if (base < 400*0.9235 && profit < 400) return {base, ss:0, medicare:0, se:0, halfDeduct:0, income:0, total:0, quarterly:0};
  const ssRoom = Math.max(0, SS_WAGE_BASE_2026 - w2);
  const ss = Math.min(base, ssRoom)*0.124, medicare = base*0.029, se = ss+medicare;
  const halfDeduct = se/2, income = Math.max(0, profit-halfDeduct)*incomePct/100;
  const total = se+income;
  return {base, ss, medicare, se, halfDeduct, income, total, quarterly: total/4};
}
function freelanceRate({income=60000, expenses=6000, hoursWeek=25, weeks=46, taxPct=25}){
  const gross = (income+expenses)/(1-taxPct/100), hours = hoursWeek*weeks;
  return {gross, hours, hourly: hours>0?gross/hours:0, day: hours>0?gross/hours*8:0};
}
function invoiceTotal(items=[], taxPct=0, discount=0){
  const sub = items.reduce((s,i)=>s+(+i.qty||0)*(+i.rate||0),0);
  const tax = (sub-discount)*taxPct/100;
  return {sub, tax, total: sub-discount+tax};
}
function earningsGoal({goal=1000, perHour=20, daysWeek=5}){
  const hours = perHour>0?goal/perHour:0; return {hours, perDay: daysWeek>0?hours/daysWeek:0};
}
const fmt = n => (n<0?'-':'')+'$'+Math.abs(n).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});
if (typeof module!=='undefined') module.exports={gigProfit,mileageDeduction,seTax,freelanceRate,invoiceTotal,earningsGoal,fmt};
