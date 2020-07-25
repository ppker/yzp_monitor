CREATE TABLE `user_info` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `study_seconds` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '累计学习时间seconds',
  `scrap` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '废料，目前通过完成任务结算废料，废料暂时是硬通货',
  `wood` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '木材, 建房子消耗',
  `stone` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '石材, 建房子消耗',
  `metal_ore` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '金属矿石, 通过熔炉炼制铁片',
  `metal_refuned` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '铁锭, 通过熔炉炼制高品质铁',
  `mark` varchar(256) NOT NULL DEFAULT '' COMMENT '备注, 可序列化为json字符串',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `user_id` (`user_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='人物基础资源表';


CREATE TABLE `base_settlement_record` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `new_value` int(11) not null default '0' comment '结算的值, 正负均可',
  `description` varchar(512) not null default '' comment '结算描述信息',
  `type` SMALLINT(5) not null default '1' comment '结算的类型, 1 => 学习时间',
  `user_id` bigint(20) unsigned NOT NULL,
  `mark` varchar(256) NOT NULL DEFAULT '' COMMENT '备注, 可序列化为json字符串',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  key `user_id` (`user_id`) using BTREE,
  key `updated_at` (`updated_at`) using BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='基础资源结算表';
