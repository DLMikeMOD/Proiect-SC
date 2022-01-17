<?php


require (dirname(__FILE__) . '/FreshsalesAnalytics.php');

FreshsalesAnalytics::init(array(
   'domain' =>  "http://localhost.freshsales-dev.com/dlmike:3000",
    'app_token' => "d583fb147e3555a65315e4d1b06f562a"
));
FreshsalesAnalytics::identify(array(
    'identifier' => "john@abc.com",
    'Last name' => "Doe",
    'company' => array(
    	'Name' => "Sample Company"
    ),
    'deal' => array(
    	'Name' => "Sample Deal"
    )
));
FreshsalesAnalytics::trackEvent(array(
    'identifier' => 'john@abc.com',
    'name' => 'Sample Event Name',
    'prop1' => 'value1', //Custom Property
    'prop2' => 'value2' //Custom Property
));
FreshsalesAnalytics::trackPageView(array(
   'identifier' => 'john@abc.com',
    'url' => 'http://www.sample.com'
));
?>