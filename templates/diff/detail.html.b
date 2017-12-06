{% extends 'basic.html' %}
{% load staticfiles %}
{% block main %}
<script src="{% static 'vendor/chart.js/Chart.min.js' %}"></script>
<script src="https://cdn.hcharts.cn/highcharts/highcharts.js"></script>
  <!-- Area Chart Example-->
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-area-chart"></i> Area Chart Example</div>
        <div class="card-body">
	<div class="table-responsive">
               <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                 <thead>
                  <tr>
                  <th>完成进度</th>
                  <th>自备数据</th>
                  <th>比对词数</th>
                  <th>备注信息</th>
                  <th>创建人员</th>
                  <th>创建时间</th>
                  <th>查看</th>
                  <th>操作</th>
                  </tr>
                 </thead>
                 <tbody>
		 <tr>
                  <td>Tiger Nixon</td>
                  <td>System Architect</td>
                  <td>Edinburgh</td>
                  <td>61</td>
                  <td>2011/04/25</td>
                  <td>$320,800</td>
                  <td>$320,800</td>
                  <td>$320,800</td>
                </tr>
                <tr>
                  <td>Garrett Winters</td>
                  <td>Accountant</td>
                  <td>Tokyo</td>
                  <td>63</td>
                  <td>2011/07/25</td>
                  <td>2011/07/25</td>
                  <td>2011/07/25</td>
                  <td>$170,750</td>
                </tr>
                <tr>
                  <td>Ashton Cox</td>
                  <td>Junior Technical Author</td>
                  <td>Junior Technical Author</td>
                  <td>Junior Technical Author</td>
                  <td>San Francisco</td>
                  <td>66</td>
                  <td>2009/01/12</td>
                  <td>$86,000</td>
                </tr>
                 </tbody>
                </table>
        </div>
        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
      </div>
      <div class="card mb-3">
        <div class="card-header">
          <i class="fa fa-area-chart"></i> Diff Top Chart</div>
        <div class="card-body">
        <div id="DiffTopChart" style="min-width:400px;height:400px"></div>	
	  <script>
		var op={
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: 'Diff TOP'
		    },
		    xAxis: {
		        //categories:  ['top4', 'top9', 'top8', 'top7', 'top6', 'top5', 'top10', 'top3', 'top2', 'top1'],
		        categories:[
				{% for module in diff_top_keylist %}
                            		"{{module}}",
                        	{% endfor %}
				],
		        crosshair: true
		    },
		    yAxis: {
		        min: 0,
		        title: {
		            text: 'value'
		        }
		    },
		    credits:{
		        enabled: false // 禁用版权信息
		    },
		    tooltip: {
		        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		        footerFormat: '</table>',
		        shared: true,
		        useHTML: true
		    },
		    plotOptions: {
		        column: {
		            pointPadding: 0.2,
		            borderWidth: 0,
		            dataLabels: {
		                enabled: true,
		                // ,allowOverlap 默认是 false，即不允许数据标签重叠
		            }
		        },
		    },
		    series: [{
		        name: '东京',
		        data: {{ diff_top_value }} 
		    }]
		};
		chart = Highcharts.chart('DiffTopChart', op);

          </script>
        </div>
        <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
      </div>
    
      <div class="row">
        <div class="col-lg-6">
          <!-- Example Bar Chart Card-->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fa fa-bar-chart"></i> diff分类统计</div>
            <div class="card-body">
	      <div id="DiffClassifiedChart" style="min-width:400px;height:400px"></div>
	      <script>
		var options={
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: ''
		    },
		    xAxis: {
		        categories:[
				{% for k,v in diff_classified_dict.items %}
                            		"{{k}}",
                        	{% endfor %}
				],
		        crosshair: true
		    },
		    yAxis: {
		        min: 0,
		        title: {
		            text: 'value'
		        }
		    },
		    credits:{
		        enabled: false // 禁用版权信息
		    },
		    tooltip: {
		        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		        footerFormat: '</table>',
		        shared: true,
		        useHTML: true
		    },
		    plotOptions: {
		        column: {
		            pointPadding: 0.2,
		            borderWidth: 0,
		            dataLabels: {
		                enabled: true,
		                // ,allowOverlap 默认是 false，即不允许数据标签重叠
		            }
		        },
		    },
		    series: [{
		        data:  [
                                {% for k,v in diff_classified_dict.items %}
                                        {{ v }},
                                {% endfor %}
                                ],
		    }]
		};
		chart = Highcharts.chart('DiffClassifiedChart', options);
          </script>
            </div>
            <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
          </div>
        </div>
        <div class="col-lg-6">
          <!-- Example Pie Chart Card-->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fa fa-pie-chart"></i> query分类统计</div>
            <div class="card-body">
	      <div id="QueryClassifiedChart" style="min-width:400px;height:400px"></div>
	      <script>
		var options={
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: ''
		    },
		    xAxis: {
		        categories:[
				{% for k,v in query_classified_dict.items %}
                            		"{{k}}",
                        	{% endfor %}
				],
		        crosshair: true
		    },
		    yAxis: {
		        min: 0,
		        title: {
		            text: 'value'
		        }
		    },
		    credits:{
		        enabled: false // 禁用版权信息
		    },
		    tooltip: {
		        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		        footerFormat: '</table>',
		        shared: true,
		        useHTML: true
		    },
		    plotOptions: {
		        column: {
		            pointPadding: 0.2,
		            borderWidth: 0,
		            dataLabels: {
		                enabled: true,
		                // ,allowOverlap 默认是 false，即不允许数据标签重叠
		            }
		        },
		    },
		    series: [{
		        data:  [
                                {% for k,v in query_classified_dict.items %}
                                        {{ v }},
                                {% endfor %}
                                ],
		    }]
		};
		chart = Highcharts.chart('QueryClassifiedChart', options);
          </script>
            </div>
            <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
          </div>
        </div>

      <div class="row">
        <div class="col-lg-6">
          <!-- Example Bar Chart Card-->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fa fa-bar-chart"></i> wenda.so.com影响统计(dcg得分对比)</div>
            <div class="card-body">
	      <div id="wenda_so_influence_Chart" style="min-width:400px;height:400px"></div>
	      <script>
		var options={
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: ''
		    },
		    xAxis: {
		        categories:[
				{% for k,v in wenda_so_influence.items %}
                            		"{{k}}",
                        	{% endfor %}
				],
		        crosshair: true
		    },
		    yAxis: {
		        min: 0,
		        title: {
		            text: 'value'
		        }
		    },
		    credits:{
		        enabled: false // 禁用版权信息
		    },
		    tooltip: {
		        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		        footerFormat: '</table>',
		        shared: true,
		        useHTML: true
		    },
		    plotOptions: {
		        column: {
		            pointPadding: 0.2,
		            borderWidth: 0,
		            dataLabels: {
		                enabled: true,
		                // ,allowOverlap 默认是 false，即不允许数据标签重叠
		            }
		        },
		    },
		    series: [{
		        data:  [
                                {% for k,v in wenda_so_influence.items %}
                                        {{ v }},
                                {% endfor %}
                                ],
		    }]
		};
		chart = Highcharts.chart('wenda_so_influence_Chart', options);
          </script>
            </div>
            <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
          </div>
        </div>
        <div class="col-lg-6">
          <!-- Example Pie Chart Card-->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fa fa-pie-chart"></i> zhidao.baidu.com影响统计(dcg得分对比)</div>
            <div class="card-body">
	      <div id="zhidao_baidu_influence_Chart" style="min-width:400px;height:400px"></div>
	      <script>
		var options={
		    chart: {
		        type: 'column'
		    },
		    title: {
		        text: ''
		    },
		    xAxis: {
		        categories:[
				{% for k,v in zhidao_baidu_influence.items %}
                            		"{{k}}",
                        	{% endfor %}
				],
		        crosshair: true
		    },
		    yAxis: {
		        min: 0,
		        title: {
		            text: 'value'
		        }
		    },
		    credits:{
		        enabled: false // 禁用版权信息
		    },
		    tooltip: {
		        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
		        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
		        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
		        footerFormat: '</table>',
		        shared: true,
		        useHTML: true
		    },
		    plotOptions: {
		        column: {
		            pointPadding: 0.2,
		            borderWidth: 0,
		            dataLabels: {
		                enabled: true,
		                // ,allowOverlap 默认是 false，即不允许数据标签重叠
		            }
		        },
		    },
		    series: [{
		        data:  [
                                {% for k,v in zhidao_baidu_influence.items %}
                                        {{ v }},
                                {% endfor %}
                                ],
		    }]
		};
		chart = Highcharts.chart('zhidao_baidu_influence_Chart', options);
          </script>
            </div>
            <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
          </div>
        </div>

      </div>
    </div>
    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fa fa-angle-up"></i>
    </a>
</div>
<script type="text/javascript" src="http://cdn.hcharts.cn/jquery/jquery-1.8.3.min.js"></script>

<script type="text/javascript" src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>

<script type="text/javascript" src="http://cdn.hcharts.cn/highcharts/exporting.js"></script>

<div id="container1" style="min-width:700px;height:400px"></div>
{% endblock main %}}
