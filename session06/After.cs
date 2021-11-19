using System;
using System.Collections.Generic;
using System.Linq;
#nullable enable

namespace BeforeAndAfter.After
{

    public class ArticleStatus {
        public int Id { get; set; }
        public string Name { get; set; }
        public ArticleStatus(string name)
        {
            Name = name;
        }
    }

    public class Article {
        public bool? HiddenByReviewer { get; set; }
        public ArticleStatus Status { get; set; } = new ArticleStatus("draft");
        public long ReviewCode { get; set; }
        public string Name { get; set; }
        public Article(string name)
        {
            Name = name;
        }
    }

    public class UserFilter {
        public string Value { get; set; }
        public string Logic { get; set; } = "or";
        public string Operator { get; set; } = "contains";

        public UserFilter(string value)
        {
            Value = value;
        }

        public bool IsBasicFilter() {
            return Logic.Equals("or") && Operator.Equals("contains");
        }

        public IEnumerable<Article> RunFilter(IEnumerable<Article> data) {
            if (IsBasicFilter()) {
                return(
                    data.Where(
                        t => ( 
                            t.Name.Contains(this.Value, StringComparison.OrdinalIgnoreCase) ||
                            string.Format("THING#{0}", t.ReviewCode.ToString().PadLeft(10, '0')).Contains(this.Value, StringComparison.OrdinalIgnoreCase)
                        )
                    )
                );
            } else {
                return data;
            }
        }
    }
    
    public enum TabEnum {
        WorkInProgress,
        SubmittedForReview,
        Accepted,
        Completed
    }

    public class Column {
        public static Column Make(TabEnum col) {
            return col switch
            {
                TabEnum.Accepted => new AcceptedColumn(),
                TabEnum.Completed => new CompletedColumn(),
                _ => new Column(),
            };
        }
        public virtual IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return data;
        }
        public virtual IEnumerable<Article> RunUserFilter(IEnumerable<Article> data, UserFilter user_filter) {
            return data;
        }
        public IEnumerable<Article> RunBothFilters(IEnumerable<Article> data, UserFilter user_filter ) {
            return RunUserFilter(RunColumnFilter(data), user_filter);
        }
    }

    public abstract class FilteringColumn : Column {
        public override IEnumerable<Article> RunUserFilter(IEnumerable<Article> data, UserFilter user_filter) {
            return user_filter.RunFilter(data);
        }
    }

    public class AcceptedColumn : FilteringColumn {
        public override IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return data.Where(p => !p.HiddenByReviewer.HasValue || !p.HiddenByReviewer.Value);
        }
    }

    public class CompletedColumn : FilteringColumn {
        public override IEnumerable<Article> RunColumnFilter(IEnumerable<Article> data) {
            return(
                data.Where(
                    p => (
                        (p.HiddenByReviewer.HasValue == true && p.HiddenByReviewer.Value == true) ||
                        (p.Status != null && p.Status.Id == 9)
                    )
                )
            );
        }
    }

    public class Exercise {
        private static IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter user_filter, Column column) {
            if (user_filter == null || column == null) throw new ArgumentNullException();
            return column.RunBothFilters(dataToFilter, user_filter);
        }       
        public static IEnumerable<Article> FilterProposals(IEnumerable<Article> dataToFilter, UserFilter? user_filter, TabEnum col) {
            return FilterProposals(dataToFilter, user_filter ?? new UserFilter("") { Logic = "" }, Column.Make(col));
        }
    }
}